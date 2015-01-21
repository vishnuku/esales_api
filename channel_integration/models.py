from django.db import models
from django.utils.translation import ugettext_lazy as _


class ChannelIntegration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    site = models.CharField(max_length=100, blank=True, default='')
    merchant_id = models.CharField(max_length=100, blank=True, default='')
    marketplace_id = models.CharField(max_length=100, blank=True, default='')
    merchant_name = models.CharField(max_length=100, blank=False, unique=True)
    access_key = models.CharField(max_length=100, blank=True, default='')
    secret_key = models.CharField(max_length=100, blank=True, default='')
    sync_status = models.SmallIntegerField(max_length=1, blank=True, default=0)
    status = models.BooleanField(default=True, verbose_name=_('Is Enabled'))

    class Meta:
        ordering = ('created',)


class Amazon(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    user = models.CharField(max_length=100, blank=True, default='')
    merchant_id = models.CharField(max_length=100, blank=True, default='')
    marketplace_id = models.CharField(max_length=100, blank=True, default='')
    access_key = models.CharField(max_length=100, blank=True, default='')
    secret_key = models.CharField(max_length=100, blank=True, default='')
    status = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
    created = models.DateTimeField(auto_now_add=True)


class AmazonInventory(models.Model):
    channel = models.ForeignKey(ChannelIntegration)
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
    product_id = models.CharField(max_length=100, blank=True, default='')
    bid_for_featured_placement = models.CharField(max_length=100, blank=True, default='')
    add_delete = models.CharField(max_length=100, blank=True, default='')
    pending_quantity = models.CharField(max_length=100, blank=True, default='')
    fulfillment_channel = models.CharField(max_length=100, blank=True, default='')