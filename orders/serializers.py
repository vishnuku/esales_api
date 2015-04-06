from rest_framework import serializers
from inventory.models import AmazonOrders
from inventory.serializers import ProductOrderSerializer


class AmazonOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonOrders


    productorder = ProductOrderSerializer(many=True, read_only=True)

    # tracks = serializers.SlugRelatedField(
    #         many=True,
    #         read_only=True,
    #         slug_field='title'
    #      )
    # AmazonOrdersSerializer


    class Meta:
        model = AmazonOrders
        fields = ('id', 'amazonorderid', 'buyername', 'buyername', 'buyeremail', 'ordertype', 'numberofitemsshipped', 'numberofitemsunshipped',
                  'paymentmethod', 'orderstatus', 'saleschannel', 'amount', 'marketplaceid', 'fulfillmentchannel',
                  'shipservicelevel', 'address', 'productorder')
        depth = 1
