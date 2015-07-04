# from django.shortcuts import render
from boto.mws.connection import MWSConnection
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mptt.forms import TreeNodeChoiceField
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import authentication, permissions

from .serializers import ChannelSerializer, AmazonProductSerializer, AmazonOrdersSerializer, \
    AmazonOrdersSerializerWithOneASINPic
from .models import Channel
from inventory.models import AmazonProduct, Product, AmazonOrders, ProductListingConfigurator, ChannelCategory
from tasks import amazon_request_report, amazon_get_order_live, amazon_get_order
from utils import amz_product_feed, amz_inventory_feed, amz_price_feed, amz_image_feed, amz_relationship_feed, \
    get_mws_conn

import logging

logger = logging.getLogger(__name__)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def channels(request):
    """
    List all code channels, or create a new channel.
    """
    if request.method == 'GET':
        #TODO: need to implement user based get.
        channels = Channel.objects.all()
        try:
            if request.GET.get('mktp') and request.GET.get('mktp') > 0:
                channels = channels.filter(marketplace__exact=int(request.GET.get('mktp')))
        except Exception as e:
            print (e)

        serializer = ChannelSerializer(channels, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # 'name','site','merchant_id','marketplace_id','merchant_name','status'
        '''data['name'] = 'test-user'
        data['merchant_id'] = data['merchantId']
        data['marketplace_id'] = data['marketplaceId']
        data['merchant_name'] = data['merchantName']
        data['aceess_key'] = data['accesskey']
        data['secret_key'] = data['secretkey']
        {"name":"amazo","site":"us","merchant_id":"A38K7PJXEQJHF2","marketplace_id":"ATVPDKIKX0DER","access_key":"AKIAID5MYRLFUQVQ26HQ","secret_key":"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","merchant_name":"amz"}
        '''


        serializer = ChannelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'OPTIONS':
        return HttpResponse(status=200)


@csrf_exempt
def channel(request, pk):
    """
    Retrieve, update or delete a code channel.
    """
    try:
        channel = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChannelSerializer(channel)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChannelSerializer(channel, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        channel.delete()
        return HttpResponse(status=204)

    elif request.method == 'OPTIONS':
        return HttpResponse(status=200)

@csrf_exempt
def inventory(request, pk):
    """
    Retrieve, update or delete a code channel.
    """
    try:
        channel = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return HttpResponse(status=404)

    try:
        inventory = AmazonProduct.objects.filter(channel=channel)
    except AmazonProduct.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AmazonProductSerializer(inventory, many=True)
        return JSONResponse(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = ChannelIntegrationSerializer(channel, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data)
    #     return JSONResponse(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     channel.delete()
    #     return HttpResponse(status=204)

    elif request.method == 'OPTIONS':
        return HttpResponse(status=200)


def sync(request, pk):
    """

    :param request:
    :type request:
    :param pk:
    :type pk:
    :return:
    :rtype:
    """
    amz = {}
    try:
        ch = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id
        amz["cid"] = pk
        amz["uid"] = request.user
        ch.sync_status = 1
        ch.save()
        # amazon_request_report.delay(amz)
        # amazon_get_report_vish(amz, '1111')
        return HttpResponse(status=200)


class InventorySync(generics.ListCreateAPIView):
    """
    Doc String
    """
    queryset = AmazonProduct.objects.all()
    model = AmazonProduct
    serializer_class = AmazonProductSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        """

        :param request:
        :type request:
        :param pk:
        :type pk:
        :return:
        :rtype:
        """

        amz = {}
        try:
            ch = Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':

            amz["akey"] = ch.access_key
            amz["skey"] = ch.secret_key
            amz["mid"] = ch.merchant_id
            amz["mpid"] = ch.marketplace_id
            amz["cid"] = pk
            amz["uid"] = request.user
            ch.sync_status = 1
            ch.save()
            amazon_request_report.delay(amz, '_GET_MERCHANT_LISTINGS_DATA_')
            return HttpResponse(status=200)


class OrderSync(generics.ListCreateAPIView):
    """
    Doc String
    """
    queryset = AmazonOrders.objects.all()
    model = AmazonOrders
    serializer_class = AmazonOrdersSerializerWithOneASINPic
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, format=None):
        """

        :param request:
        :type request:
        :param pk:
        :type pk:
        :return:
        :rtype:
        """
        # amz = {}
        # try:
        #     ch = Channel.objects.get(pk=pk)
        # except Channel.DoesNotExist:
        #     return HttpResponse(status=404)
        #
        # amz["akey"] = ch.access_key
        # amz["skey"] = ch.secret_key
        # amz["mid"] = ch.merchant_id
        # amz["mpid"] = ch.marketplace_id
        # amz["cid"] = pk
        # amz["uid"] = request.user

        # ch.sync_status = 1
        # ch.save()
        #TODO set for date
        # amazon_get_order_live.delay(amz)
        logger.info('order sync process init.')
        amazon_get_order.delay(request.user)
        logger.info('order sync process completed.')
        print('Order synced')
        data = {"success": "true"}
        return Response(data, status=status.HTTP_200_OK)


class ListingProducts_original(generics.ListCreateAPIView):
    """
    Doc String
    """
    queryset = AmazonProduct.objects.all()
    model = AmazonProduct
    serializer_class = AmazonProductSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, chid, format=None):
        amz = {}
        products = []
        serializer = AmazonProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     # serializer.save()
        #     data = {"success": "true"}
        #     return Response(data, status=status.HTTP_200_OK)
        #create product feed
        ch = Channel.objects.get(pk=3)
        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id

        data = JSONParser().parse(request)
        ps = request.POST.getlist('pids')

        if not ps:
            ps = data['pids']
        ps = [ps]
        for p in ps:
            pr = {}
            p_obj = Product.objects.get(id=int(p))
            pr['sku'] = p_obj.sku
            pr['title'] = p_obj.name
            pr['brand'] = "Iphone tampered glass"
            pr['desc'] = "Sample description iphone tampered glass"
            pr['bulletpoint1'] = "Bullet Pount sample"
            pr['bulletpoint2'] = "Bullet Pointt sample"
            pr['MSRP'] = p_obj.retail_price
            pr['manufacturer'] = 'zuang ho'
            pr['itemtype'] = 'cell-phone-accessories'
            pr['upc'] = '4015643103939'
            pr['qnty'] = p_obj.stock
            pr['ffl'] = "1"
            pr['imgtype'] = "Main" #Alternate/Swatch
            pr['imgloc'] = "http://example.com" #Alternate/Swatch

            products.append(pr)

        pfeedxml = amz_product_feed(amz, products)
        ifeedxml = amz_inventory_feed(amz, products)
        prfeedxml = amz_price_feed(amz, products)
        imfeedxml = amz_image_feed(amz, products)

        # con = get_mes_conn(amz)
        # rr = con.submit_feed(FeedType='_POST_PRODUCT_DATA_', PurgeAndReplace=True, FeedContent=pfeedxml,
        #                      content_type='text/xml')
        #
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus
        #
        # rr = con.submit_feed(FeedType='_POST_INVENTORY_AVAILABILITY_DATA_', PurgeAndReplace=True, FeedContent=ifeedxml,
        #                      content_type='text/xml')
        #
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus
        #
        # rr = con.submit_feed(FeedType='_POST_PRODUCT_PRICING_DATA_', PurgeAndReplace=True, FeedContent=prfeedxml,
        #                      content_type='text/xml')
        #
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        # rr = con.submit_feed(FeedType='_POST_PRODUCT_IMAGE_DATA_', PurgeAndReplace=True, FeedContent=pfeedxml,
        #                      content_type='text/xml')

        # print rr
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus
        # print pfeedxml
        # print ifeedxml
        # print prfeedxml
        # print imfeedxml
        # print request.POST

        data = {"success": "true"}
        return Response(data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingProducts(generics.ListCreateAPIView):
    """
    Doc String
    """
    queryset = AmazonProduct.objects.all()
    model = AmazonProduct
    serializer_class = AmazonProductSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, chid, format=None):
        """

        :param request:
        :type request:
        :param chid:
        :type chid:
        :param format:
        :type format:
        :return:
        :rtype:
        """
        amz = {}
        products = []
        data = JSONParser().parse(request)
        # print data
        ps = data['pids']
        cfid = data['configurator_id']
        # print "cfid: ", cfid
        try:
            cf_obj = ProductListingConfigurator.objects.get(pk=int(cfid))
        except Exception as e:
            # raise "Configuratator error"
            # print "cf ex", e
            pass
        print cf_obj
        itemtypes = []

        for cid in cf_obj.category3[1:-1].split(','):
            try:
                obj = ChannelCategory.objects.get(pk=int(cid))
                itemtypes.append(obj.item_type_keyword)
            except:
                pass

        ch = Channel.objects.get(pk=chid)
        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id

        for p in ps:
            pr = {}
            p_obj = Product.objects.get(id=int(p))
            pr['sku'] = p_obj.sku
            pr['title'] = p_obj.name
            pr['brand'] = p_obj.brand
            pr['desc'] = p_obj.desc
            pr['bulletpoint1'] = p_obj.bullet_point
            pr['bulletpoint2'] = p_obj.bullet_point
            pr['MSRP'] = p_obj.retail_price
            pr['manufacturer'] = p_obj.manufacturer
            pr['itemtype'] = p_obj.category.name
            pr['ucodetype'] = p_obj.ucodetype
            pr['ucodevalue'] = p_obj.ucodevalue
            pr['qnty'] = 100
            pr['ffl'] = "1"
            pr['imgtype'] = "Main" #Alternate/Swatch
            pr['imgloc'] = "http://example.com" #Alternate/Swatch
            pr['pdata'] = cf_obj.category1.item_type_keyword
            pr['ptype'] = cf_obj.category2.item_type_keyword
            pr['itemtypes'] = itemtypes

            products.append(pr)

        pfeedxml = amz_product_feed(amz, products)
        ifeedxml = amz_inventory_feed(amz, products)
        prfeedxml = amz_price_feed(amz, products)
        imfeedxml = amz_image_feed(amz, products)

        con = get_mws_conn(amz)
        rr = con.submit_feed(FeedType='_POST_PRODUCT_DATA_', PurgeAndReplace=True, FeedContent=pfeedxml,
                             content_type='text/xml')

        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        rr = con.submit_feed(FeedType='_POST_INVENTORY_AVAILABILITY_DATA_', PurgeAndReplace=True, FeedContent=ifeedxml,
                             content_type='text/xml')

        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        rr = con.submit_feed(FeedType='_POST_PRODUCT_PRICING_DATA_', PurgeAndReplace=True, FeedContent=prfeedxml,
                             content_type='text/xml')

        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        # rr = con.submit_feed(FeedType='_POST_PRODUCT_IMAGE_DATA_', PurgeAndReplace=True, FeedContent=imfeedxml,
        #                      content_type='text/xml')

        # rfeedxml = amz_relationship_feed(amz, type, parent_sku, child_skus)
        # rr = con.submit_feed(FeedType='_POST_PRODUCT_RELATIONSHIP_DATA_', PurgeAndReplace=True, FeedContent=rfeedxml,
        # content_type='text/xml')

        # print rr
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus
        # print pfeedxml
        # print ifeedxml
        # print prfeedxml
        # print imfeedxml
        # print request.POST
        data = {"success": "true"}
        return Response(data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryOrder(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = AmazonOrdersSerializerWithOneASINPic

    def get_queryset(self):
        queryset = AmazonOrders.objects.all()
        queryset = queryset.filter(id=self.kwargs['pk'])
        return queryset
