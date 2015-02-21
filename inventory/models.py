import os
from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from integration.models import Channel


class Category(MPTTModel):
    """
    Models for category of the product
    """
    name = models.CharField(max_length=50, unique=True, blank=True)
    status = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_category')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_category')
    user = models.ForeignKey(User)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class ProductType(models.Model):
    """
    Product Type
    TODO: USE in future no current use
    """
    name = models.CharField(max_length=50, unique=True)


class Product(models.Model):
    """
    Model for product
    TODO: Restructure as per standarrd
    """
    name = models.CharField(max_length=255, blank=False)
    purchase_price = models.FloatField()
    retail_price = models.FloatField()
    tax_price = models.FloatField(blank=True, default=0)
    sku = models.CharField(max_length=100, blank=False, unique=True)
    barcode = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    minimum_stock_level = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    meta_data = models.TextField()
    origin = models.CharField(max_length=55, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_product')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_product')
    user = models.ForeignKey(User)


class Images(models.Model):
    """
    Model to hold the images for product
    """
    product = models.ForeignKey(Product, default=1, related_name='images')
    image = models.ImageField(upload_to='product/images/upload/%Y/%m/%d')
    is_main = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_images')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_images')
    user_id = models.ForeignKey(User)

    class Meta:
        ordering = ('created',)

    def get_image_abs_path(self):
        """

        :return:
        :rtype:
        """
        return os.path.join(settings.MEDIA_ROOT, self.image.name)

    def __unicode__(self):
        return '%s' % self.image


class Sync(models.Model):
    """
    Keep tracks of sync request
    """
    task = models.CharField(max_length=255, blank=False)
    state = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=255, blank=False)
    channel = models.ForeignKey(Channel)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_sync')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_sync')
    user_id = models.ForeignKey(User)


class AmazonProduct(models.Model):
    """
    To hold the amazon inventory
    """
    channel = models.ForeignKey(Channel)
    product = models.ForeignKey(Product)
    item_name = models.CharField(max_length=100, blank=True, default='')
    item_description = models.CharField(max_length=100, blank=True, default='')
    listing_id = models.CharField(max_length=100, blank=True, default='')
    seller_sku = models.CharField(max_length=100, blank=True, default='')
    price = models.CharField(max_length=100, blank=True, default='')
    quantity = models.CharField(max_length=100, blank=True, default='')
    open_date = models.CharField(max_length=100, blank=True, default='')
    image_url = models.CharField(max_length=100, blank=True, default='')
    item_is_marketplace = models.CharField(max_length=100, blank=True, default='')
    product_id_type = models.CharField(max_length=100, blank=True, default='')
    zshop_shipping_fee = models.CharField(max_length=100, blank=True, default='')
    item_note = models.CharField(max_length=100, blank=True, default='')
    item_condition = models.CharField(max_length=100, blank=True, default='')
    zshop_category1 = models.CharField(max_length=100, blank=True, default='')
    zshop_browse_path = models.CharField(max_length=100, blank=True, default='')
    zshop_storefront_feature = models.CharField(max_length=100, blank=True, default='')
    asin1 = models.CharField(max_length=100, blank=True, default='')
    asin2 = models.CharField(max_length=100, blank=True, default='')
    asin3 = models.CharField(max_length=100, blank=True, default='')
    will_ship_internationally = models.CharField(max_length=100, blank=True, default='')
    expedited_shipping = models.CharField(max_length=100, blank=True, default='')
    zshop_boldface = models.CharField(max_length=100, blank=True, default='')
    bid_for_featured_placement = models.CharField(max_length=100, blank=True, default='')
    add_delete = models.CharField(max_length=100, blank=True, default='')
    pending_quantity = models.CharField(max_length=100, blank=True, default='')
    fulfillment_channel = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_amzp')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_amzp')
    user_id = models.ForeignKey(User)


