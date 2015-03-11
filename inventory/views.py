#from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, ProductWithImagesSerializer,\
    InventoryCSVSerializer, ChannelCategorySerializer
from .models import Category, Product, Images, CSV, ChannelCategory
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class CategoryList(generics.ListCreateAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List the category details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    """
    List all the products
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageList(generics.ListCreateAPIView):
    """
    List image related to a product
    """
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,) #TOOD Remove This block once fixed on client size
    model = Images
    serializer_class = ImageSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Images.objects.all()
        product = self.request.QUERY_PARAMS.get('product', None)
        if product is not None:
            queryset = queryset.filter(product_id=product)
        return queryset

    # @csrf_exempt
    # def post(self, request, format=None):
    #     serializer = ImageSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         data = {"success": "true"}
    #         return Response(data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductImageDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List info about a image
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class ProductWithImagesList(generics.ListAPIView):
    """
    List of product with images
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductWithImagesSerializer


class ProductWithImagesDetails(generics.RetrieveAPIView):
    """
    Details of product
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductWithImagesSerializer


class InventoryProductsViaCSV(generics.ListCreateAPIView):
    """
    This class handle Product CSV upload by user for bulk inventory listing.
    """
    # authentication_classes = (authentication.TokenAuthentication,)

    queryset = CSV.objects.all()
    serializer_class = InventoryCSVSerializer
    permission_classes = (permissions.AllowAny,)


class ChannelCategoryList(generics.ListAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ChannelCategory.objects.all()
    serializer_class = ChannelCategorySerializer

    def get(self, request, *args, **kwargs):
        print 'Get called'
        ch = ChannelCategory.objects
        dir(ch)
        return self.list(request, *args, **kwargs)
