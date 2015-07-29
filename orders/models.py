from django.db import models
from django.contrib.auth.models import User
from inventory.models import AmazonOrders

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from jsonfield import JSONField


class Filter(MPTTModel):
    name = models.CharField(max_length=50, blank=True, default='', unique=True)
    # query = JSONField()
    query = models.TextField(blank=True, null=True)
    column = models.TextField(blank=True, null=True)
    logic = models.TextField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_order_filter')
    updated_by = models.ForeignKey(User, related_name='updated_by_order_filter')
    user = models.ForeignKey(User)
    filter_count = models.IntegerField(null=True)

    def __unicode__(self):
        return '%s' % self.name


'''
Model name: OrderShippingDetail()
Description: This model is holding the Oder Shipping Detail
@field: order [ForeignKey of AmazonOrders]
@field: ship_date  [DateField]
@field: shipping_method  [String, MaxLength:50]
@field: shipping_service  [String, MaxLength:100]
@field: tracking_no  [Json Feld]
@field: created_on  [DateField]
@field: updated_on  [DateField]
@field: created_by  [User Object:id]
@field: updated_by  [User Object:id]
@field: user        [User Object:id]
'''


class OrderShippingDetail(models.Model):
    order = models.ForeignKey(AmazonOrders)
    ship_date = models.DateField(null=True)
    shipping_method = models.CharField(max_length=50, null=True)
    shipping_service = models.CharField(max_length=100, null=True)
    tracking_no = JSONField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_order_shipping_detail')
    updated_by = models.ForeignKey(User, related_name='updated_by_order_shipping_detail')
    user = models.ForeignKey(User)
