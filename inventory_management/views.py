#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework import permissions

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def categories(request):
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

@csrf_exempt
def category(request, pk):
    try:
        category_object = ProductCategory.objects.get(pk=pk)
    except ProductCategory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InventoryProductCategorySerializer(category_object)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InventoryProductCategorySerializer(category_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=404)
    elif request.method == 'DELETE':
        category_object.delete()
        return HttpResponse(status=204)

''' This function is used to add new inventory item to db and fetch and return on basis of request method
 '''
@csrf_exempt
def products(request):
    if request.method == 'GET':
        products_list = InventoryProducts.objects.all().select_related('image')
        serializer = InventoryProductSerializer(products_list, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InventoryProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def product(request, pk):
    try:
        product_object = InventoryProducts.objects.get(pk=pk)
    except InventoryProducts.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InventoryProductSerializer(product_object)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InventoryProductSerializer(product_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product_object.delete()
        return HttpResponse(status=204)

    elif request.method == 'OPTIONS':
        return HttpResponse(status=200)


class InventoryProductImageList(generics.ListCreateAPIView):
    queryset = InventoryProductImages.objects.all()
    model = InventoryProductImages
    serializer_class = InventoryProductImageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class InventoryProductImageDetails(generics.RetrieveAPIView):
    queryset = InventoryProductImages.objects.all()
    serializer_class = InventoryProductImageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class InventoryProductWithImages(generics.ListAPIView):
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductWithImagesSerializer
    permission_classes = [
        permissions.AllowAny
    ]
