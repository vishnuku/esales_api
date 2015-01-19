from rest_framework import serializers
from .models import ChannelIntegration, Amazon, AmazonInventory


class ChannelIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelIntegration
        fields = ('name', 'site', 'merchant_id', 'marketplace_id', 'aceess_key', 'secret_key', 'merchant_name',
                  'status')


class AmazonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon
        fields = ('user', 'merchant_id', 'marketplace_id', 'aceess_key', 'secret_key', 'status')


class AmazonInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AmazonInventory
        # fields = ('item_name', 'id')
        fields = (
            'item_name', 'item_description', 'listing_id', 'seller_sku', 'price', 'quantity', 'open_date', 'image_url',
            'item_is_marketplace', 'product_id_type', 'zshop_shipping_fee', 'item_note', 'item_condition',
            'zshop_category1', 'zshop_browse_path', 'zshop_storefront_feature', 'asin1', 'asin2', 'asin3',
            'will_ship_internationally', 'expedited_shipping', 'zshop_boldface', 'product_id', 'bid_for_featured_placement',
            'add_delete', 'pending_quantity', 'fulfillment_channel')