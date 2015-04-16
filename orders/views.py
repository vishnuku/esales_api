from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import authentication, permissions
from inventory.models import AmazonOrders, ProductOrder
from orders import serializers
from orders.serializers import AmazonOrdersSerializerPost
import json
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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.AmazonOrdersSerializerPost
        return serializers.AmazonOrdersSerializerList

    def perform_create(self, serializer):
        serializer.save(address=json.dumps(self.request.data['address']), user=self.request.user, created_by=self.request.user, updated_by=self.request.user)
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