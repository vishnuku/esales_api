from rest_framework import serializers
from rest_framework.fields import empty
from inventory.models import AmazonOrders, Images
from inventory.serializers import ProductOrderSerializer
from orders.models import Filter


class AmazonOrdersSerializerList(serializers.ModelSerializer):
    # return all associated products, due to extra overhead we will get this data on order click.
    #productorder = ProductOrderSerializer(many=True, read_only=True)

    address = serializers.SerializerMethodField('return_json_address')
    product_pic = serializers.SerializerMethodField('return_order_product_pic')

    def return_json_address(self, AmazonOrders):
        return AmazonOrders.address

    def return_order_product_pic(self, AmazonOrders):
        # pictures = Images.objects.filter(product_id=AmazonOrders.amazonproduct)
        # if len(pictures) > 0:
        #     return str(pictures[0].image)
        # else:
        #     return str('NA')
        return str('NA')

    class Meta:
        model = AmazonOrders
        fields = ('id', 'amazonorderid', 'buyername', 'buyername', 'buyeremail', 'ordertype', 'numberofitemsshipped', 'numberofitemsunshipped',
                  'paymentmethod', 'orderstatus', 'saleschannel', 'amount', 'marketplaceid', 'fulfillmentchannel',
                  'shipservicelevel', 'address', 'product_pic', 'purchasedate', 'lastupdatedate', 'amazonproduct')
        depth = 1

class AmazonOrdersSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = AmazonOrders
        fields = ('id', 'amazonorderid', 'buyername', 'buyername', 'buyeremail', 'ordertype', 'numberofitemsshipped', 'numberofitemsunshipped',
                  'paymentmethod', 'orderstatus', 'saleschannel', 'amount', 'marketplaceid', 'fulfillmentchannel',
                  'shipservicelevel', 'purchasedate', 'lastupdatedate', 'amazonproduct')


# class RecursiveField(serializers.Serializer):
#     def to_native(self, value):
#         return self.parent.to_native(value)

class ChildrenSerializer(serializers.ModelSerializer):

    class Meta:
            model = Filter
            # fields = ('id', 'name', 'query', 'parent')
            fields = ('id', 'name', 'query')


# class FilterSerializer(serializers.ModelSerializer):
#     parent = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#             model = Filter
#             fields = ('id', 'name', 'query', 'parent', 'children')
#             depth=2
#
#             def get_related_field(self, model_field):
#                 return FilterSerializer()
#

class FilterSerializerList(serializers.ModelSerializer):
    leaf = serializers.SerializerMethodField('is_leaf')
    query = serializers.SerializerMethodField('return_json_query')

    def is_leaf(self, Filter):
        return Filter.is_leaf_node()

    def to_representation(self, obj):
            #Add any self-referencing fields here (if not already done)
            if 'branches' not in self.fields:
                self.fields['children'] = FilterSerializerList(obj, many=True)
            return super(FilterSerializerList, self).to_representation(obj)

    def return_json_query(self, Filter):
        return eval(str(Filter.query))

    class Meta:
            model = Filter
            fields = ('id', 'name', 'query', 'parent', 'leaf')


class FilterSerializerPost(serializers.ModelSerializer):

    def to_representation(self, obj):
            #Add any self-referencing fields here (if not already done)
            if 'branches' not in self.fields:
                self.fields['children'] = FilterSerializerPost(obj, many=True)
            return super(FilterSerializerPost, self).to_representation(obj)


    class Meta:
            model = Filter
            fields = ('id', 'name', 'query', 'parent')

