from django.contrib.auth.models import User
from rest_framework import serializers
from integration.serializers import AmazonOrdersSerializerWithOneASINPic

from .models import Category, Product, Images, CSV, ChannelCategory, ProductListingConfigurator, Warehouse, WarehouseBin, \
    ProductOrder, AmazonOrders, Product_Bundle


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'status', 'created_on')


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
                  'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode', 'stock_quantity', 'min_stock_quantity',
                  'sold_quantity', 'category', 'channel', 'meta_data', 'origin', 'created_on')


class ImageSerializer(serializers.ModelSerializer):
    """
    Image Serializer
    """
    class Meta:
        model = Images


class ProductWithImagesSerializer(serializers.ModelSerializer):
    """
    Product with Image Serializer
    """
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'description', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
                  'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode', 'stock_quantity', 'min_stock_quantity',
                  'sold_quantity', 'category', 'channel', 'meta_data', 'misc_data', 'origin', 'created_on', 'field2', 'field8', 'images')


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

    class Meta:
        model = WarehouseBin
        fields = ('id', 'name', 'warehouse', 'stock_quantity', 'sold_quantity', 'min_stock_quantity', 'product', 'warehouse_detail')


class ProductOrderSerializer(serializers.ModelSerializer):
    '''
    This method returned data on basis of order item.
    '''
    products = ProductWithImagesSerializer(source='product',read_only=True)
    warehousebins = WarehouseBinSerializer(source='warehousebin',read_only=True)

    class Meta:
        model = ProductOrder
        fields = ('id', 'products', 'warehousebins', 'quantity', 'status', 'warehousebin')


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


class BundleProductSerializer(serializers.ModelSerializer):
    items = ProductSerializer(source='item', read_only=True)

    class Meta:
        model = Product_Bundle
        fields = ('id', 'price', 'qty', 'item', 'product', 'items')
