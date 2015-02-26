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

class InventoryProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryProductImages



class InventoryProductWithImagesSerializer(serializers.ModelSerializer):
    #images = serializers.StringRelatedField(many=True)
    images = InventoryProductImageSerializer(many=True)

    class Meta:
        model = InventoryProducts
        fields = ('id', 'product_sku', 'name', 'purchase_price', 'retail_price', 'tax_price', 'meta_data',
                  'category_id', 'barcode', 'stock_value', 'minimum_stock_level', 'user_id', 'status', 'created',
                  'images')