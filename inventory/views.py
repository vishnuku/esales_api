#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from .serializers import ImageSerializer, ProductSerializer, ProductWithImagesSerializer, CategorySerializer
from .models import Images, Product, Category
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
        category_object = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category_object)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category_object, data=data)
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
        products_list = Product.objects.all().select_related('image')
        serializer = ProductSerializer(products_list, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def product(request, pk):
    try:
        product_object = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product_object)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product_object.delete()
        return HttpResponse(status=204)

    elif request.method == 'OPTIONS':
        return HttpResponse(status=200)


class ProductImageList(generics.ListCreateAPIView):
    """
    Doc String
    """
    queryset = Images.objects.all()
    model = Images
    serializer_class = ImageSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ProductImageDetails(generics.RetrieveAPIView):
    """
    Doc String
    """
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ProductWithImagesList(generics.ListAPIView):
    """
    Doc String
    """
    queryset = Product.objects.all()
    serializer_class = ProductWithImagesSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ProductWithImagesDetails(generics.RetrieveAPIView):
    """
    Doc String
    """
    queryset = Product.objects.all()
    serializer_class = ProductWithImagesSerializer
    permission_classes = [
        permissions.AllowAny
    ]
