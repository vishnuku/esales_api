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

from .serializers import ChannelSerializer, AmazonProductSerializer, AmazonOrdersSerializer
from .models import Channel
from inventory.models import AmazonProduct, Product, AmazonOrders
from tasks import amazon_request_report, amazon_get_order_live
from utils import amz_product_feed, amz_inventory_feed, amz_price_feed, amz_image_feed




# Create your views here.

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
        channels = Channel.objects.all()
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
    serializer_class = AmazonOrdersSerializer
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
        amz = {}
        try:
            ch = Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            return HttpResponse(status=404)

        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id
        amz["cid"] = pk
        amz["uid"] = request.user
        # ch.sync_status = 1
        # ch.save()
        #TODO set for date
        amazon_get_order_live.delay(amz)
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

        # con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
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
        print pfeedxml
        print ifeedxml
        print prfeedxml
        print imfeedxml
        print request.POST

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
        amz = {}
        products = []
        serializer = AmazonProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     # serializer.save()
        #     data = {"success": "true"}
        #     return Response(data, status=status.HTTP_200_OK)
        #create product feed
        ch = Channel.objects.get(pk=chid)
        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id
        data = JSONParser().parse(request)
        ps = request.POST.getlist('pids')

        if not ps:
            ps = data['pids']
        #ps = [ps]
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

            products.append(pr)

        pfeedxml = amz_product_feed(amz, products)
        ifeedxml = amz_inventory_feed(amz, products)
        prfeedxml = amz_price_feed(amz, products)
        imfeedxml = amz_image_feed(amz, products)

        con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
        rr = con.submit_feed(FeedType='_POST_PRODUCT_DATA_', PurgeAndReplace=True, FeedContent=pfeedxml,
                             content_type='text/xml')

        print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        rr = con.submit_feed(FeedType='_POST_INVENTORY_AVAILABILITY_DATA_', PurgeAndReplace=True, FeedContent=ifeedxml,
                             content_type='text/xml')

        print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        rr = con.submit_feed(FeedType='_POST_PRODUCT_PRICING_DATA_', PurgeAndReplace=True, FeedContent=prfeedxml,
                             content_type='text/xml')

        print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus

        # rr = con.submit_feed(FeedType='_POST_PRODUCT_IMAGE_DATA_', PurgeAndReplace=True, FeedContent=pfeedxml,
        #                      content_type='text/xml')

        # print rr
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedSubmissionId
        # print rr.SubmitFeedResult.FeedSubmissionInfo.FeedProcessingStatus
        print pfeedxml
        print ifeedxml
        print prfeedxml
        print imfeedxml
        print request.POST
        TreeNodeChoiceField()
        data = {"success": "true"}
        return Response(data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
