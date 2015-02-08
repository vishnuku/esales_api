from rest_framework import serializers
from .models import ProductCategory, Products

class InventoryProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'category_name', 'status', 'created', 'user_id')

class InventoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'product_sku', 'name', 'purchase_price', 'retail_price', 'tax_price', 'meta_data',
                  'category', 'barcode', 'user_id', 'created')