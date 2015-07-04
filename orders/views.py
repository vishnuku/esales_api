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
import logging

logger = logging.getLogger(__name__)

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
            fl = self.request.QUERY_PARAMS.get('fl', None) if (self.request.QUERY_PARAMS.get('fl', None)).isdigit() else None
            queryset = None
            if fl is not None:
                logger.info("Got filter id: %s", fl)
                try:
                    filter = Filter.objects.get(pk=int(fl))
                    if filter:
                        ancestor_logic = Q()                                  #Create Q object to hold other query
                        #If filter is only root node
                        if filter.is_root_node():
                            ancestor_logic = pickle.loads(filter.logic)             #Deserilize the filter logic
                            logger.info("Filter has only root node, Logic: %s", ancestor_logic)

                        #If filter has parents
                        else:
                            for filter_data in filter.get_ancestors(False,True):  #Get all parents including self
                                filter_logic = pickle.loads(filter_data.logic)    #Deserilize the filter logic
                                if ancestor_logic.__len__()==0:
                                    ancestor_logic = filter_logic
                                else:
                                    ancestor_logic = ancestor_logic & filter_logic

                            logger.info("Filter has parents, Logic: %s", ancestor_logic)

                        if ancestor_logic:
                            queryset = AmazonOrders.objects.filter(ancestor_logic)  #pass the query object to filter
                            logger.info("Filter query, Query: %s", queryset.query)


                except Exception as e:
                    logger.error("In queryset exception : %s",e)
            else:
                queryset = AmazonOrders.objects.all()
                logger.info("Filter not passed, Processing full Query: %s", queryset.query)

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
    # queryset = Filter.objects.all()
    # serializer_class = FilterSerializer
    model = Filter

    def get_queryset(self):
        queryset = Filter.objects.all()
        if self.request.method == 'GET':
            logger.info("Get data of all parent")
            queryset = queryset.filter(parent__isnull=True)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FilterSerializerPost
        return FilterSerializerList

    def perform_create(self, serializer):
        query = json.dumps(self.request.data['query'])
        column = json.dumps(self.request.data['column'])

        #Create Instance of Filter logic
        filter_logic = FilterLogic()
        query_obj = filter_logic.parse_response(query, 0, '')

        #Serilize query object to save it
        pickle_obj = pickle.dumps(filter_logic.condition_data) if filter_logic.condition_data else None

        serializer.save(query=query, column=column, logic=pickle_obj, user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


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

        #Create Instance of Filter logic
        filter_logic = FilterLogic()
        query_obj = filter_logic.parse_response(query, 0, '')

        #Serilize query object to save it
        pickle_obj = pickle.dumps(filter_logic.condition_data) if filter_logic.condition_data else None

        serializer.save(query=query, logic=pickle_obj, user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class FilterLogic():
    OperatorMapping = {
        'isbetween':               '__range',
        'isnotbetween':            '__range',  #TODO work for this
        'equals':                  '__exact',
        'doesnotequal':            '__exact',
        'islessthan':              '__lt',
        'islessthanorequalto':     '__lte',
        'isgreaterthan':           '__gt',
        'isgreaterthanorequalto' : '__gte',
        'beginswith':              '__istartswith',
        'endswith':                '__iendswith',
        'any':                     'operator.or_',
        'all':                     'operator.and_',
        'and':                     'and',
        'or':                      'or',
        'none':                    'or'
    }

    final_data = []
    branch_data = []
    condition_data = Q()
        # branch_join_type=None

    def parse_response(self, json_string, branch_level, branch_join_type):
        print "json:       " + json_string
        print '***branch_level: ',branch_level
        content = json.loads(str(json_string))
        for key, value in content.iteritems():
            if key == 'branches':
                print 'in brance %s',key
                # print self.condition_data.__len__()
                if type(value) == type(['']):
                    branch_level += 1
                    for sub_value in value:
                        branch_join_type = sub_value['branchJoinType']

                        strg = str(json.dumps(sub_value))
                        self.branch_data.append(strg)

                        self.parse_response(strg, branch_level, branch_join_type)

            elif key == 'conditions':
                print 'in conditions %s',key
                if type(value) == type(['']):
                    strg = str(json.dumps(value))
                    data = self.parse_condition(strg, content['conditionJoinType'])
                    print 'data******',data
                    print 'Branch Join Type %s',branch_join_type
                    if self.condition_data.__len__()==0:
                        self.condition_data = data
                    if branch_join_type and self.condition_data.__len__()>0:
                        if branch_join_type == 'and':
                            self.condition_data = self.condition_data & data
                        elif branch_join_type == 'or':
                            self.condition_data = self.condition_data | data
                        elif branch_join_type == 'none':
                            self.condition_data = self.condition_data | data


                    # if branch_join_type and self.condition_data.__len__()>0:
                        # self.condition_data.append(self.OperatorMapping[branch_join_type])
                    # self.condition_data.append(data)


            else:
                print value


            # if content.has_key('branchJoinType'):
            #     if data:
            #         final_data=final_data.__and__(data)
            #     print 'final_data******',final_data


    def parse_condition(self, condition_string, conditionJoinType):
        print "______________start condition json_______________"
        print conditionJoinType, condition_string
        content = json.loads(str(condition_string))

        py_data = []
        for data in content:
            if data['conditionKey'] == 'isbetween':
                py_data.append(Q((data['lhsOperandKey']+self.OperatorMapping[data['conditionKey']], (data['conditionValue1'], data['conditionValue2']))))
            elif data['conditionKey'] == 'doesnotequal':
                py_data.append(~Q((data['lhsOperandKey']+self.OperatorMapping[data['conditionKey']], data['conditionValue'])))
            else:
                py_data.append(Q((data['lhsOperandKey']+self.OperatorMapping[data['conditionKey']], data['conditionValue'])))

        if py_data:
            q = reduce(eval(self.OperatorMapping[conditionJoinType]), py_data)

            print q
            return q
        #
        # q = reduce(eval(self.OperatorMapping[conditionJoinType]), py_data)
        #
        # print q
        # print self.OperatorMapping[conditionJoinType]
        # print "______________end condition json_______________"
        # return q