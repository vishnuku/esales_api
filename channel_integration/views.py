# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ChannelIntegrationSerializer
from .models import ChannelIntegration


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
        serializer = ChannelIntegrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


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
