import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from tasks import map_order_product_warehouse

from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, ProductWithImagesSerializer,\
    InventoryCSVSerializer, ChannelCategorySerializer, ProductListingConfiguratorSerializer, WarehouseSerializer, \
    WarehouseBinSerializer, ProductOrderSerializer, OrderProductSerializer, BundleProductSerializer, InventorySerializer
from .models import Category, Product, Images, CSV, ChannelCategory, ProductListingConfigurator, Warehouse, \
    WarehouseBin, ProductOrder, AmazonOrders, Product_Bundle, Inventory
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView, ListCreateBulkUpdateAPIView

logger = logging.getLogger(__name__)


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


class InventoryList(generics.ListCreateAPIView):
    """
    List all the Inventory
    This View will manage only local inventory
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InventorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user.id, updated_by=self.request.user.id)

    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a `username` query parameter in the URL.
            """
            queryset = Inventory.objects.all()
            name = self.request.QUERY_PARAMS.get('name', None)
            sku = self.request.QUERY_PARAMS.get('sku', None)

            if name is not None:
                queryset = queryset.filter(name__icontains=name)
            elif sku is not None:
                queryset = queryset.filter(sku=sku)
            return queryset



class InventoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Inventory details
    This View will manage only local inventory
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ProductList(generics.ListCreateAPIView):
    """
    List all the products
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)

    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a `username` query parameter in the URL.
            """
            queryset = Product.objects.all()
            name = self.request.QUERY_PARAMS.get('name', None)
            sku = self.request.QUERY_PARAMS.get('sku', None)
            type = self.request.QUERY_PARAMS.get('type', None)

            if type is not None:
                queryset = queryset.filter(product_type=type)
            if name is not None:
                queryset = queryset.filter(name__icontains=name)
            elif sku is not None:
                queryset = queryset.filter(sku=sku)
            return queryset



class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InventoryImageList(generics.ListCreateAPIView):
    """
    List image related to a product
    """
    permission_classes = (permissions.AllowAny,) #TOOD Remove This block once fixed on client size
    model = Images
    serializer_class = ImageSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Images.objects.all()
        inventory = self.request.QUERY_PARAMS.get('inventory', None)
        if inventory is not None:
            queryset = queryset.filter(inventory_id=inventory)
        return queryset

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class InventoryImageDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List info about a image
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


# not using it, because its converted from ProductImageList to InventoryImageList
class ProductImageList(generics.ListCreateAPIView):
    """
    List image related to a product
    """
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

# not using it, because its converted from ProductImageDetails to InventoryImageDetails
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

        if 'warehouse' in self.kwargs and 'inventory' in self.kwargs:
            if int(self.kwargs['inventory']) == 0:
                queryset = queryset.filter(warehouse=self.kwargs['warehouse']).filter(inventory__isnull=True)
            elif int(self.kwargs['inventory']) == 1:
                queryset = queryset.filter(warehouse=self.kwargs['warehouse']).filter(inventory__isnull=False)

        elif 'inventory' in self.kwargs:
            queryset = queryset.filter(inventory=self.kwargs['inventory'])

        elif 'warehouse' in self.kwargs:
            queryset = queryset.filter(warehouse=self.kwargs['warehouse'])

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

    def perform_update(self, serializer):
        serializer.save()

        try:
            map_order_product_warehouse.delay(pid=serializer.data['products']['id'], binid=serializer.data['warehousebins']['id'])
        except Exception as e:
            #TODO add logger
            print 'In Exception',e
            pass


class OrderProductDetails(generics.RetrieveAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = AmazonOrders.objects.all()
    serializer_class = OrderProductSerializer


class BundleProductList(ListBulkCreateUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product_Bundle.objects.all()
    serializer_class = BundleProductSerializer

    def update_bundle_product(self, id, stock_quantity):
        product = Product.objects.get(pk=id)

        if product:
            product.product_type = 2
            product.stock_quantity = stock_quantity
            product.save()
            logger.debug('Product Bundle updated:')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)
        self.update_bundle_product(self.request.data[0]['product'], self.request.data[0]['bundle_product_qty'])

    def get_queryset(self):
        queryset = Product_Bundle.objects.all()
        if 'product' in self.kwargs:
            queryset = queryset.filter(product=self.kwargs['product'])

        return queryset

    def patch(self, request, *args, **kwargs):

        for it in self.request.data:
            obj = Product_Bundle.objects.get(pk=it['id'])
            obj.price = it['price']
            obj.qty = it['qty']
            obj.save()

        self.update_bundle_product(self.request.data[0]['product'], self.request.data[0]['bundle_product_qty'])

        data = {'success': 'true'}
        return Response(data, status=status.HTTP_200_OK)




class BundleProductDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product_Bundle.objects.all()
    serializer_class = BundleProductSerializer
