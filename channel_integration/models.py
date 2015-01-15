from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# Create your models here.
class ChannelIntegration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    site = models.CharField(max_length=100, blank=True, default='')
    merchant_id = models.CharField(max_length=100, blank=True, default='')
    marketplace_id = models.CharField(max_length=100, blank=True, default='')
    merchant_name = models.CharField(max_length=100, blank=False, unique=True)
    status = models.BooleanField(default=True, verbose_name=_('Is Enabled'))

    class Meta:
        ordering = ('created',)
