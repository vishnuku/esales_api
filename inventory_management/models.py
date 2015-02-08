from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=False, unique=True)
    status = models.SmallIntegerField(max_length=1, default=0)
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=False)

    class Meta:
        ordering = ('created',)

''' Inventory Item model
        '''
class Products(models.Model):
    product_sku = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    purchase_price = models.FloatField(blank=False)
    retail_price = models.FloatField(blank=False)
    tax_price = models.FloatField(blank=True, default=0)
    meta_data = models.TextField(blank=False)
    category = models.IntegerField(blank=False)
    barcode = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)