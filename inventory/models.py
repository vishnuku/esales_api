import os

from django.conf import settings
from django.db import models
from json_field import JSONField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from integration.models import Channel

UCODETYPE = (
    ('ISBN', 'ISBN'),
    ('UPC', 'UPC'),
    ('EAN', 'EAN'),
)

class Category(MPTTModel):
    """
    Models for category of the product
    """
    name = models.CharField(max_length=50, unique=True, blank=True)
    status = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
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
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, blank=False, unique=True)
    ucodetype = models.CharField(max_length=20, blank=True, choices=UCODETYPE)
    ucodevalue = models.CharField(max_length=50, blank=True)
    barcode = models.CharField(max_length=200)
    purchase_price = models.FloatField(blank=True, default=0)
    retail_price = models.FloatField(blank=True, default=0)
    tax_price = models.FloatField(blank=True, default=0)
    stock_quantity = models.IntegerField(default=0)
    min_stock_quantity = models.IntegerField(default=0)
    sold_quantity = models.IntegerField(default=0)
    pending_quantity = models.IntegerField(default=0)
    image_url = models.CharField(max_length=100, blank=True, default='')
    shipping_fee = models.CharField(max_length=100, blank=True, default='')
    will_ship_internationally = models.CharField(max_length=100, blank=True, default='')
    expedited_shipping = models.CharField(max_length=100, blank=True, default='')
    brand = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    bullet_point = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category)
    meta_data = models.TextField()
    origin = models.CharField(max_length=55, blank=True, null=True)
    field1 = models.CharField(max_length=50, blank=True, null=True)
    field2 = models.CharField(max_length=50, blank=True, null=True)
    field3 = models.CharField(max_length=50, blank=True, null=True)
    field4 = models.CharField(max_length=50, blank=True, null=True)
    field5 = models.CharField(max_length=50, blank=True, null=True)
    field6 = models.CharField(max_length=50, blank=True, null=True)
    field7 = models.CharField(max_length=50, blank=True, null=True)
    field8 = models.CharField(max_length=50, blank=True, null=True)
    field9 = models.CharField(max_length=50, blank=True, null=True)
    field10 = models.CharField(max_length=50, blank=True, null=True)
    misc_data = JSONField()
    warehouse = JSONField()
    channel = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_product')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_product')
    user = models.ForeignKey(User)



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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_amzp')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_amzp')
    user = models.ForeignKey(User)

#
# class Product(models.Model):
#     """
#     Model for product
#     TODO: Restructure as per standarrd
#     """
#     name = models.CharField(max_length=255, blank=False)
#     brand = models.CharField(max_length=255, blank=True, null=True)
#     desc = models.TextField(blank=True, null=True)
#     bullet_point = models.TextField(blank=True, null=True)
#     manufacturer = models.CharField(max_length=255, blank=True)
#     ucodetype = models.CharField(max_length=255, blank=True, choices=UCODETYPE)
#     ucodevalue = models.CharField(max_length=255, blank=True)
#     purchase_price = models.FloatField()
#     retail_price = models.FloatField()
#     tax_price = models.FloatField(blank=True, default=0)
#     sku = models.CharField(max_length=100, blank=False, unique=True)
#     barcode = models.CharField(max_length=200)
#     stock = models.IntegerField(default=0)
#     minimum_stock_level = models.IntegerField(default=0)
#     category = models.ForeignKey(Category)
#     meta_data = models.TextField()
#     origin = models.CharField(max_length=55, blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
#     created_by = models.ForeignKey(User, related_name='created_by_user_product')
#     updated_by = models.ForeignKey(User, related_name='updated_by_user_product')
#     user = models.ForeignKey(User)
#

class Images(models.Model):
    """
    Model to hold the images for product
    """
    product = models.ForeignKey(Product, default=1, related_name='images')
    image = models.ImageField(upload_to='product/images/upload/%Y/%m/%d')
    is_main = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=1, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_images')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_images')
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('created_on',)

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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_sync')
    updated_by = models.ForeignKey(User, related_name='updated_by_user_sync')
    user = models.ForeignKey(User)


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError(u'File type not supported')

class CSV(models.Model):

    """
    To hold inventory csv files upload by user.
    """
    name = models.FileField(upload_to=settings.MEDIA_ROOT+'csv/%Y-%m-%d', max_length=200, validators=[validate_file_extension])
    status = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_csv')
    updated_by = models.ForeignKey(User, related_name='updated_by_csv')
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('created_on',)


class ChannelCategory(MPTTModel):
    """
    Models for category of the product
    """
    node_id = models.BigIntegerField(blank=False)
    node_path = models.CharField(max_length=200, blank=False)
    item_type_keyword = models.CharField(max_length=200, blank=False)
    channel = models.CharField(max_length=20, blank=False)
    status = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_channel_category')
    updated_by = models.ForeignKey(User, related_name='updated_by_channel_category')
    user = models.ForeignKey(User)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return '%s' % self.node_path


class AmazonOrders(models.Model):
    """
    Doc
    """
    amazonproduct = models.CharField(blank=True, null=True, max_length=50)
    amazonorderid = models.CharField(blank=False, null=True, max_length=50, db_index=True)
    buyername = models.CharField(blank=False, null=True, max_length=50)
    buyeremail = models.EmailField(blank=False, null=True)
    ordertype = models.CharField(blank=False, null=True, max_length=50, db_index=True)
    numberofitemsshipped = models.SmallIntegerField(null=True)
    numberofitemsunshipped = models.SmallIntegerField(null=True)
    paymentmethod = models.CharField(blank=False, null=True, max_length=50)
    orderstatus = models.CharField(blank=False, null=True, max_length=50)
    saleschannel = models.CharField(blank=False, null=True, max_length=50, db_index=True)
    amount = models.CharField(blank=False, null=True, max_length=50)
    marketplaceid = models.CharField(blank=False, null=True, max_length=50, db_index=True)
    fulfillmentchannel = models.CharField(blank=False, null=True, max_length=50)
    shipservicelevel = models.CharField(blank=False, null=True, max_length=50)
    address = JSONField()
    purchasedate = models.DateTimeField(db_index=True)
    lastupdatedate = models.DateTimeField(db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True, db_index=True)
    created_by = models.ForeignKey(User, related_name='created_by_amazonorders')
    updated_by = models.ForeignKey(User, related_name='updated_by_amazonorders')
    user = models.ForeignKey(User)

    def create_from_dict(self, data, exempt=()):
        """

        :param data:
        :type data:
        :param exception:
        :type exception:
        :return:
        :rtype:
        """
        for k in data.keys():
            if k not in exempt:
                setattr(self, k, data[k])

    def __str__(self):
        return '%s' % self.amazonorderid


class ProductListingConfigurator(models.Model):
    """Extra information for product configuration

    """

    name = models.CharField(max_length=255, blank=False)
    marketplace = models.CharField(max_length=255, blank=False)
    marketplace_domain = models.CharField(max_length=255, blank=False)
    category1 = models.ForeignKey(ChannelCategory, related_name='category1_product_listing_conf')
    category2 = models.ForeignKey(ChannelCategory, related_name='category2_product_listing_conf')
    category3 = models.CharField(max_length=255, blank=False)
    status = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_product_listing_conf1')
    updated_by = models.ForeignKey(User, related_name='updated_by_product_listing_conf2')
    user = models.ForeignKey(User)

    def __str__(self):
        return '%s' % self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=105, blank=False)
    address = models.CharField(max_length=255, blank=True)
    town = models.CharField(max_length=105, blank=True)
    country = models.CharField(max_length=105, blank=True)
    status = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_warehouse')
    updated_by = models.ForeignKey(User, related_name='updated_by_warehouse')
    user = models.ForeignKey(User)

    def __str__(self):
        return '%s' % self.name


class WarehouseBin(models.Model):
    warehouse = models.ForeignKey(Warehouse)
    product = models.ForeignKey(Product, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)
    min_stock_quantity = models.IntegerField(default=0)
    sold_quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=105, blank=False)
    status = models.SmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_warehouse_product')
    updated_by = models.ForeignKey(User, related_name='updated_by_warehouse_product')
    user = models.ForeignKey(User)

    def __str__(self):
        return '%s' % self.name


class ProductOrder(models.Model):
    product = models.ForeignKey(Product)
    amazonorders = models.ForeignKey(AmazonOrders, related_name='productorder')
    warehousebin = models.ForeignKey(WarehouseBin, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20, blank=True, default='')
    message = models.CharField(max_length=50, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_product_order')
    updated_by = models.ForeignKey(User, related_name='updated_by_product_order')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('product', 'amazonorders')

    def __unicode__(self):
        return '%s' % self.product.name
