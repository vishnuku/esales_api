from rest_framework import serializers
from .models import *


class InventoryProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'category_name', 'status', 'created', 'user_id')


class InventoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryProducts
        fields = ('id', 'product_sku', 'name', 'purchase_price', 'retail_price', 'tax_price', 'meta_data',
                  'category_id', 'barcode', 'stock_value', 'minimum_stock_level', 'user_id', 'status', 'created')


class InventoryProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryProductImages
        fields = ('id', 'image', 'is_main', 'status', 'created', 'inventory_product_id')
        inventory_product_id = serializers.Field(source='inventory_product_id.name')
