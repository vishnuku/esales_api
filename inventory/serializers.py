from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, Images, CSV, ChannelCategory


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'status', 'created')


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer
    """
    class Meta:
        model = Product


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
                  'category', 'barcode', 'stock', 'minimum_stock_level', 'user', 'created',
                  'images')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class InventoryCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV

class ChannelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelCategory