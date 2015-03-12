from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models


MARKETPLACES = (
    (1, 'Amazon'),
    (2, 'ebay'),
    (3, 'mkt1'),
    (4, 'mkt2'),
)


class Channel(models.Model):
    """
    Will store all the data related to market placse
    marketplace == 1. Amazon
    """
    created = models.DateTimeField(auto_now_add=True)
    marketplace = models.PositiveSmallIntegerField(choices=MARKETPLACES, default=1)
    name = models.CharField(max_length=100, blank=True, default='')
    site = models.CharField(max_length=100, blank=True, default='')
    merchant_id = models.CharField(max_length=100, blank=True, default='')
    marketplace_id = models.CharField(max_length=100, blank=True, default='')
    merchant_name = models.CharField(max_length=100, blank=False, unique=True)
    access_key = models.CharField(max_length=100, blank=True, default='')
    secret_key = models.CharField(max_length=100, blank=True, default='')
    sync_status = models.SmallIntegerField(blank=True, default=0)
    status = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_user_channel', default=1)
    updated_by = models.ForeignKey(User, related_name='updated_by_user_channel', default=1)
    user_id = models.ForeignKey(User, default=1)

    class Meta:
        ordering = ('created',)