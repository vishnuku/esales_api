from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import os
import uuid

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

def get_unique_image_file_path(instance=None, filename='dummy.jpg'):
    """
    function to determine where to save images.  assigns a uuid (random string) to each and places it
    in the images subdirectory below media.  by default, we assume the file is a .jpg
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    # TODO: 'images' is hard coded
    return os.path.join('images', filename)

class InventoryProductImages(models.Model):
    inventory_product = models.ForeignKey(InventoryProducts, default=1)
    image = models.ImageField(upload_to=get_unique_image_file_path)
    is_main = models.BooleanField(default=0)
    status = models.SmallIntegerField(default=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_image_abs_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.image.name)

    class Meta:
        ordering = ('created',)