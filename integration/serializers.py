from rest_framework import serializers
from .models import Channel, AmazonCategories
from inventory.models import AmazonProduct


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'site', 'merchant_id', 'marketplace_id', 'access_key', 'secret_key', 'merchant_name',
                  'status', 'sync_status')


class AmazonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'user', 'merchant_id', 'marketplace_id', 'access_key', 'secret_key', 'status')


class AmazonProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmazonProduct
        # fields = ('item_name', 'id')
        fields = (
            'id','item_name', 'item_description', 'listing_id', 'seller_sku', 'price', 'quantity', 'open_date', 'image_url',
            'item_is_marketplace', 'product_id_type', 'zshop_shipping_fee', 'item_note', 'item_condition',
            'zshop_category1', 'zshop_browse_path', 'zshop_storefront_feature', 'asin1', 'asin2', 'asin3',
            'will_ship_internationally', 'expedited_shipping', 'zshop_boldface', 'product', 'bid_for_featured_placement',
            'add_delete', 'pending_quantity', 'fulfillment_channel')


class AmazonCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmazonCategories