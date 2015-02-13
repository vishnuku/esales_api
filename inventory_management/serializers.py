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

''' tesing serializer for image with product '''
class InventoryProductImageSerializerTest(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    class Meta:
        model = InventoryProducts
        fields = ('id', 'images')

class InventoryProductWithImagesSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = InventoryProducts
        fields = ('id', 'product_sku', 'name', 'purchase_price', 'retail_price', 'tax_price', 'meta_data',
                  'category_id', 'barcode', 'stock_value', 'minimum_stock_level', 'user_id', 'status', 'created',
                  'images')


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')

class ImgSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = InventoryProducts
        fields = ('id', 'name', 'tracks')

''' tesing close '''