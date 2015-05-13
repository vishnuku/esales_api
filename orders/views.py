from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework import authentication, permissions
from inventory.models import AmazonOrders, ProductOrder
from orders import serializers
from orders.models import Filter
from orders.serializers import FilterSerializerPost, FilterSerializerList
import json
from inventory.models import Product
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):

        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class OrderList(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # serializer_class = AmazonOrdersSerializer

    queryset = AmazonOrders.objects.all()
    model = AmazonOrders

    def manage_inventory_on_order_received(self, order_status, item_id, order_item_qty ):
        product = Product.objects.get(pk=item_id)
        if order_status == 'shipped':
            product.stock_quantity -= order_item_qty
            product.save()


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.AmazonOrdersSerializerPost
        return serializers.AmazonOrdersSerializerList


    def perform_create(self, serializer):
        address = json.dumps(self.request.data['address'])
        address = json.loads(address)
        serializer.save(address=address, user=self.request.user, created_by=self.request.user, updated_by=self.request.user)
        amazonproducts = self.request.data['amazonproducts'] if self.request.data['amazonproducts'] else ''
        if len(amazonproducts) > 0 :
            for product in amazonproducts :
                productorder, created = ProductOrder.objects.get_or_create(product_id=product,
                                                                           amazonorders_id=serializer.data['id'],
                                                                            defaults={'quantity': '1',
                                                                             'status': 'Unshipped',
                                                                             'message': '',
                                                                             'user': self.request.user,
                                                                             'created_by': self.request.user,
                                                                             'updated_by': self.request.user})
                productorder.save()



class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Product details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = AmazonOrders.objects.all()
    serializer_class = serializers.AmazonOrdersSerializerList


class FilterList(generics.ListCreateAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Filter.objects.all()
    # serializer_class = FilterSerializer
    model = Filter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FilterSerializerPost
        return FilterSerializerList

    def perform_create(self, serializer):
        query = json.dumps(self.request.data['query'])
        serializer.save(query=query, user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class FilterDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List the Filter details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Filter.objects.all()
    # serializer_class = FilterSerializerList

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return FilterSerializerPost
        return FilterSerializerList


    def perform_update(self, serializer):
        query = json.dumps(self.request.data['query'])
        serializer.save(query=query, user=self.request.user, created_by=self.request.user, updated_by=self.request.user)
