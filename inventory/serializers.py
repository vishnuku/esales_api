from rest_framework import serializers
from .models import Category, Product, Images


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'status', 'created', 'user_id')


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer
    """
    class Meta:
        model = Product
        # fields = ('id', 'sku', 'name', 'purchase_price', 'retail_price', 'tax_price', 'meta_data',
        #           'category', 'barcode', 'stock_value', 'minimum_stock_level', 'user_id', 'status', 'created')


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
        fields = ('id', 'sku', 'name', 'purchase_price', 'retail_price', 'tax_price', 'meta_data',
                  'category', 'barcode', 'stock_value', 'minimum_stock_level', 'user_id', 'status', 'created',
                  'images')
