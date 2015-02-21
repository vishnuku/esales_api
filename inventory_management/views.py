#from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework import authentication, permissions

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ProductCategoryList(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ProductCategory.objects.all()
    serializer_class = InventoryProductCategorySerializer


class ProductCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductCategory.objects.all()
    serializer_class = InventoryProductCategorySerializer


class ProductList(generics.ListCreateAPIView):
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
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,) #TOOD Remove This block once fixed on client size
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
