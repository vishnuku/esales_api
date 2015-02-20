#from django.shortcuts import render
import token
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from rest_framework import authtoken
from rest_framework import authentication, permissions

#from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

'''
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
'''

class ProductCategoryList(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductCategory.objects.all()
    serializer_class = InventoryProductCategorySerializer


class ProductCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductCategory.objects.all()
    serializer_class = InventoryProductCategorySerializer


class ProductList(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductSerializer



class InventoryProductImageList(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    model = InventoryProductImages
    serializer_class = InventoryProductImageSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = InventoryProductImages.objects.all()
        product = self.request.QUERY_PARAMS.get('product', None)
        if product is not None:
            queryset = queryset.filter(inventory_product__id=product)
        return queryset


    def post(self, request, format=None):
        serializer = InventoryProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"success": "true"}
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InventoryProductImageDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = InventoryProductImages.objects.all()
    serializer_class = InventoryProductImageSerializer

class InventoryProductWithImagesList(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductWithImagesSerializer


class InventoryProductWithImagesDetails(generics.RetrieveAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductWithImagesSerializer
