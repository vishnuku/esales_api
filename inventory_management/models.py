from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=False, unique=True)
    status = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=False)

    class Meta:
        ordering = ('created',)

''' Inventory Item model
        '''
class InventoryProducts(models.Model):
    product_sku = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    purchase_price = models.FloatField(blank=False)
    retail_price = models.FloatField(blank=False)
    tax_price = models.FloatField(blank=True, default=0)
    meta_data = models.TextField(blank=False,)
    category_id = models.IntegerField(blank=False)
    barcode = models.CharField(max_length=200)
    stock_value = models.IntegerField(blank=False, default=0)
    minimum_stock_level = models.IntegerField(blank=False, default=0)
    user_id = models.IntegerField(blank=False)
    status = models.SmallIntegerField(default=0,blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

'''InventoryProduct Images'''
class InventoryProductImages(models.Model):
    inventory_product_id = models.ForeignKey(InventoryProducts)
    image = models.ImageField(upload_to='photos')
    is_main = models.BooleanField(default=0)
    status = models.SmallIntegerField(default=0, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)