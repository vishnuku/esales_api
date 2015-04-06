from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework import authentication, permissions

from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, ProductWithImagesSerializer,\
    InventoryCSVSerializer, ChannelCategorySerializer, ProductListingConfiguratorSerializer, WarehouseSerializer, \
    WarehouseBinSerializer, ProductOrderSerializer
from .models import Category, Product, Images, CSV, ChannelCategory, ProductListingConfigurator, Warehouse, \
    WarehouseBin, ProductOrder


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)

    #TODO: overrided default post method
    def post(self, request, *args, **kwargs):
        x = super(InventoryProductsViaCSV, self).post(request, *args, **kwargs)
        return x


class ChannelCategoryList(generics.ListAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ChannelCategorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ChannelCategory.objects.all()

        if 'catid' in self.kwargs:
            queryset = queryset.filter(channel=self.kwargs['channel'], level=self.kwargs['level'], parent_id=self.kwargs['catid'])
        elif 'level' in self.kwargs:
            queryset = queryset.filter(channel=self.kwargs['channel'], level=self.kwargs['level'])
        else:
            queryset = queryset.filter(channel=self.kwargs['channel'], level=0)

        print queryset.query
        return queryset



class ProductListingConfiguratorList(generics.ListCreateAPIView):
    """
    List all the ProductListingConfigurator
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductListingConfigurator.objects.all()
    serializer_class = ProductListingConfiguratorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class ProductListingConfiguratorDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductListingConfigurator.objects.all()
    serializer_class = ProductListingConfiguratorSerializer


class WarehouseList(generics.ListCreateAPIView):
    """
    List all the ProductListingConfigurator
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class WarehouseDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseBinList(generics.ListCreateAPIView):
    """
    List all the ProductListingConfigurator
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = WarehouseBin.objects.all()
    serializer_class = WarehouseBinSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = WarehouseBin.objects.all()

        if 'warehouse' in self.kwargs and 'product' in self.kwargs:
            if int(self.kwargs['product']) == 0:
                queryset = queryset.filter(warehouse=self.kwargs['warehouse']).filter(product__isnull=True)
            elif int(self.kwargs['product']) == 1:
                queryset = queryset.filter(warehouse=self.kwargs['warehouse']).filter(product__isnull=False)

        elif 'product' in self.kwargs:
            queryset = queryset.filter(product=self.kwargs['product'])

        return queryset



class WarehouseBinDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = WarehouseBin.objects.all()
    serializer_class = WarehouseBinSerializer


class ProductOrderList(generics.ListCreateAPIView):
    """
    List all the ProductListingConfigurator
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ProductOrder.objects.all()

        if 'order' in self.kwargs:
            queryset = queryset.filter(amazonorders=self.kwargs['order'])

        return queryset


class ProductOrderDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

