# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ChannelIntegrationSerializer, AmazonSerializer, AmazonInventorySerializer
from .models import ChannelIntegration, Amazon, AmazonInventory
from tasks import amazon_request_report


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
        channels = ChannelIntegration.objects.all()
        serializer = ChannelIntegrationSerializer(channels, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # 'name','site','merchant_id','marketplace_id','merchant_name','status'
        '''data['name'] = 'test-user'
        data['merchant_id'] = data['merchantId']
        data['marketplace_id'] = data['marketplaceId']
        data['merchant_name'] = data['merchantName']
        data['aceess_key'] = data['accesskey']
        data['secret_key'] = data['secretkey']'''

        serializer = ChannelIntegrationSerializer(data=data)
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
        channel = ChannelIntegration.objects.get(pk=pk)
    except ChannelIntegration.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChannelIntegrationSerializer(channel)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChannelIntegrationSerializer(channel, data=data)
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
        channel = ChannelIntegration.objects.get(pk=pk)
    except ChannelIntegration.DoesNotExist:
        return HttpResponse(status=404)

    try:
        inventory = AmazonInventory.objects.filter(channel=channel)
    except AmazonInventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AmazonInventorySerializer(inventory, many=True)
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
        ch = ChannelIntegration.objects.get(pk=pk)
    except ChannelIntegration.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        print ch
        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id
        amz["cid"] = pk
        ch.sync_status = 1
        ch.save()
        #amazon_request_report.delay(amz)
        return HttpResponse(status=200)