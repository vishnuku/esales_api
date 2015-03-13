from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Product, Images, CSV, ChannelCategory, ProductListingConfigurator


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
        fields = ('id', 'name', 'brand', 'desc', 'bullet_point', 'manufacturer', 'ucodetype', 'ucodevalue',
                  'purchase_price', 'retail_price', 'tax_price', 'sku', 'barcode', 'stock', 'minimum_stock_level',
                  'category', 'meta_data', 'origin', 'status', 'created')


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
        fields = ('id', 'name', 'status', 'created')


class ChannelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelCategory


class ProductListingConfiguratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListingConfigurator
        fields = ('id', 'name','marketplace','marketplace_domain','category1','category2','category3',
                  'status', 'created')
