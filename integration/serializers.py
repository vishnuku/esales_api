from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Channel
from inventory.models import AmazonProduct, AmazonOrders, Images


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

'''

'''
class AmazonOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonOrders


class AmazonOrdersSerializerWithOneASINPic(serializers.ModelSerializer):
    address = serializers.SerializerMethodField('return_json_address')
    product_pic = serializers.SerializerMethodField('return_order_product_pic')

    def return_json_address(self, AmazonOrders):
        #print foo
        return AmazonOrders.address

    def return_order_product_pic(self, AmazonOrders):
        pictures = Images.objects.filter(product_id=AmazonOrders.amazonproduct)
        if len(pictures) > 0:
            return str(pictures[0].image)
        else:
            return str('NA')

    class Meta:
        model = AmazonOrders
        fields = ('id', 'amazonorderid', 'buyername', 'buyeremail', 'ordertype', 'numberofitemsshipped', 'numberofitemsunshipped',
                  'numberofitemsunshipped', 'orderstatus', 'saleschannel', 'amount', 'marketplaceid', 'fulfillmentchannel',
                  'shipservicelevel', 'purchasedate', 'lastupdatedate', 'created_on', 'address', 'amazonproduct', 'product_pic')