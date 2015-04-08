from rest_framework import serializers
from inventory.models import AmazonOrders, Images
from inventory.serializers import ProductOrderSerializer


class AmazonOrdersSerializer(serializers.ModelSerializer):
    # return all associated products, due to extra overhead we will get this data on order click.
    #productorder = ProductOrderSerializer(many=True, read_only=True)

    address = serializers.SerializerMethodField('return_json_address')
    product_pic = serializers.SerializerMethodField('return_order_product_pic')

    def return_json_address(self, AmazonOrders):
        return AmazonOrders.address

    def return_order_product_pic(self, AmazonOrders):
        pictures = Images.objects.filter(product_id=AmazonOrders.amazonproduct)
        if len(pictures) > 0:
            return str(pictures[0].image)
        else:
            return str('NA')

    class Meta:
        model = AmazonOrders
        fields = ('id', 'amazonorderid', 'buyername', 'buyername', 'buyeremail', 'ordertype', 'numberofitemsshipped', 'numberofitemsunshipped',
                  'paymentmethod', 'orderstatus', 'saleschannel', 'amount', 'marketplaceid', 'fulfillmentchannel',
                  'shipservicelevel', 'address',  'product_pic', 'purchasedate')
        depth = 1
