from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer
from integration.serializers import AmazonOrdersSerializerWithOneASINPic

from .models import Category, Product, Images, CSV, ChannelCategory, ProductListingConfigurator, Warehouse, WarehouseBin, \
    ProductOrder, AmazonOrders, Product_Bundle, Inventory, StockIn, StockOut, Product_Inventory, Shipping_Setting, \
    ProductImages


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'status', 'created_on')


class InventoryBinSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseBin
        fields = ('id', 'name', 'stock_quantity')

class InventoryImageSerializer(serializers.ModelSerializer):
    """
    Inventory Serializer
    """
    class Meta:
        model = Images
        fields = ['id', 'image']


class InventorySerializer(serializers.ModelSerializer):
    """
    Inventory Serializer
    """
    images = InventoryImageSerializer(many=True, read_only=True)
    inventorywarehousebin = InventoryBinSerializer(many=True, read_only=True)

    class Meta:
        model = Inventory
        fields = ('id', 'name', 'brand', 'description', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
                  'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode',
                  'category', 'meta_data', 'created_on', 'item_quantity', 'sold_quantity', 'images', 'inventorywarehousebin')




# class ProductSerializer(serializers.ModelSerializer):
#     """
#     Product Serializer
#     """
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'brand', 'description', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
#                   'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode', 'stock_quantity', 'min_stock_quantity',
#                   'sold_quantity', 'category', 'channel', 'meta_data', 'origin', 'created_on', 'product_type', 'field2', 'field8','linked_inventory')


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Image Serializer
    """
    class Meta:
        model = ProductImages
        fields = ('product', 'image', 'id')



class ProductSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    Product Serializer
    """
    images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        list_serializer_class = BulkListSerializer
        fields = ('id', 'name', 'brand', 'description', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
                  'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode', 'stock_quantity', 'min_stock_quantity',
                  'sold_quantity', 'category', 'channel', 'meta_data', 'origin', 'created_on', 'product_type',
                  'parent_product', 'field2', 'field8','linked_inventory', 'images')


class ImageSerializer(serializers.ModelSerializer):
    """
    Image Serializer
    """
    class Meta:
        model = Images



class ProductInventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_Inventory
        fields = ('id', 'product', 'inventory', 'quantity')



class ProductWithImagesSerializer(serializers.ModelSerializer):
    """
    Product with Image Serializer
    """
    inventory = InventoryImageSerializer(read_only=True)
    # invetories = InventoryImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
                  'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode', 'stock_quantity', 'min_stock_quantity',
                  'sold_quantity', 'category', 'channel', 'meta_data', 'misc_data', 'origin', 'created_on', 'field2', 'field8',
                  'inventory', 'linked_inventory')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class InventoryCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = ('id', 'name', 'status', 'created_on')


class ChannelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelCategory


class ChannelCategoryForConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelCategory
        fields = ('id', 'node_path')


class ProductListingConfiguratorSerializer(serializers.ModelSerializer):
    category1_details = ChannelCategoryForConfigSerializer(source='category1', read_only=True)
    category2_details = ChannelCategoryForConfigSerializer(source='category2', read_only=True)

    class Meta:
        model = ProductListingConfigurator
        fields = ('id', 'name', 'marketplace', 'marketplace_domain', 'category1', 'category2',
                  'category3', 'status', 'created_on', 'category1_details', 'category2_details')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'address', 'country', 'town')


class WarehouseBinSerializer(serializers.ModelSerializer):
    warehouse_detail = WarehouseSerializer(source='warehouse', read_only=True)
    inventory_detail = InventorySerializer(read_only=True, source='inventory')

    class Meta:
        model = WarehouseBin
        fields = ('id', 'name', 'warehouse', 'stock_quantity', 'sold_quantity', 'min_stock_quantity', 'inventory', 'inventory_detail', 'warehouse_detail')


class ProductOrderSerializer(serializers.ModelSerializer):
    #products = ProductWithImagesSerializer(source='product', read_only=True)
    products = ProductSerializer(source='product', read_only=True)
    warehousebins = WarehouseBinSerializer(source='warehousebin', read_only=True)

    class Meta:
        model = ProductOrder
        fields = ('id', 'products', 'warehousebins', 'quantityordered', 'warehousebin', 'quantityordered', 'quantityshipped', 'itemprice')


class ProductOrderSerializer2(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder

class OrderProductSerializer(serializers.ModelSerializer):
    productorder = ProductOrderSerializer(many=True, read_only=True)

    # tracks = serializers.SlugRelatedField(
    #         many=True,
    #         read_only=True,
    #         slug_field='title'
    #      )
    # AmazonOrdersSerializer


    class Meta:
        model = AmazonOrders
        fields = ('id', 'amazonorderid', 'buyername', 'productorder')
        depth = 1


class ProductInventorySerializer(serializers.ModelSerializer):

    product_i_inventory = InventorySerializer(source='inventory', read_only=True)

    class Meta:
        model = Product_Inventory
        fields = ('id', 'product', 'inventory', 'quantity', 'product_i_inventory')


class BundleProductSerializer(serializers.ModelSerializer):
    #items = InventorySerializer(source='item', read_only=True)
    # bundle = ProductSerializer(source='product', read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    product_i_product = ProductInventorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        #fields= ('id', 'images', 'product_i_product')




class StockInSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockIn
        fields = ('id', 'product', 'inventory', 'amazonorders', 'warehousebin', 'quantity')


class StockOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockOut
        fields = ('id', 'product', 'inventory', 'amazonorders', 'warehousebin', 'quantity')


class ShippingSettingSerializer(serializers.ModelSerializer):
    orderid = serializers.CharField(read_only=True)

    class Meta:
        model = Shipping_Setting
        fields = ('id', 'hashcode', 'weight1', 'weight1_unit', 'weight2', 'weight2_unit', 'length',
                  'height', 'width', 'dimension_unit', 'd_standard', 'd_expedited', 'd_second_day', 'd_single_day',
                  'd_economy', 'i_standard', 'i_expedited',  'i_economy', 'orderid')


