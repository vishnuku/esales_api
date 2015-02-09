#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
# Create your views here.

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def category(request):
    if request.method == 'GET':
        categories = ProductCategory.objects.all()
        serializer = InventoryProductCategorySerializer(categories, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)  ## parese request data to json format.
        serializer = InventoryProductCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

''' This function is used to add new inventory item to db and fetch and return on basis of request method
 '''
@csrf_exempt
def Products(request):
    if request.method == 'GET':
        products = InventoryProducts.objects.all()
        serializer = InventoryProductSerializer(products, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InventoryProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def Product(request, pk):
    try:
        product = InventoryProducts.objects.get(pk=pk)
    except InventoryProducts.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InventoryProductSerializer(product)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        print data
        serializer = InventoryProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

    elif request.method == 'OPTIONS':
        return HttpResponse(status=200)

