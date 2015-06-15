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
from django.db.models import Q
import pickle
import operator

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

    model = AmazonOrders


    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a `username` query parameter in the URL.
            """
            fl = self.request.QUERY_PARAMS.get('fl', None)
            queryset = AmazonOrders.objects.all()

            if fl is not None:
                try:
                    filter = Filter.objects.get(pk=int(fl))
                    if filter:
                        logic = pickle.loads(filter.logic)
                        queryset = AmazonOrders.objects.filter(logic)
                        print queryset.query

                except Exception as e:
                    print e

            return queryset


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
        column = json.dumps(self.request.data['column'])
        fl = FilterLogic()
        a = fl.parse_response(query)
        b = pickle.dumps(a)
        serializer.save(query=query, column=column, logic=b, user=self.request.user, created_by=self.request.user, updated_by=self.request.user)



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

class FilterLogic():
    OperatorMapping = {
        'isbetween':           '__range',
        'equals':              '__eq',
        'islessthanorequalto': '__lte',
        'any':                 'operator.or_',
        'all':                 'operator.and_'
    }

    def parse_response(self, json_string):
        print "json:       " + json_string
        content = json.loads(str(json_string))
        branch_level = 0
        final_data=""
        for key, value in content.iteritems():
            print key
            if key == 'branches':
                print 'in brance %s',key
                if type(value) == type(['']):
                    branch_level += 1
                    for sub_value in value:
                        strg = str(json.dumps(sub_value))
                        self.parse_response(strg)
            elif key == 'conditions':
                print 'in conditions %s',key
                if type(value) == type(['']):
                    strg = str(json.dumps(value))
                    final_data = self.parse_condition(strg, content['conditionJoinType'])

            else:
                print '***branch_level: ',branch_level
                print value

        return final_data

    def parse_condition(self, condition_string, conditionJoinType):
        print "______________start condition json_______________"
        print conditionJoinType, condition_string
        content = json.loads(str(condition_string))

        py_data = []
        for sub_value in content:
            self.build_logic(sub_value, py_data)

        q_list = [Q(x) for x in py_data]

        q = reduce(eval(self.OperatorMapping[conditionJoinType]), q_list)


        print q
        print "______________end condition json_______________"
        return q


    def build_logic(self, data, py_data):
        if data['conditionKey'] == 'isbetween':
            py_data.append((data['lhsOperandKey']+self.OperatorMapping[data['conditionKey']], (data['conditionValue1'], data['conditionValue2'])))
        else:
            py_data.append((data['lhsOperandKey']+self.OperatorMapping[data['conditionKey']], data['conditionValue']))



