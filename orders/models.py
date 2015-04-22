from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Filter(MPTTModel):
    name = models.CharField(max_length=20, blank=True, default='', unique=True)
    query = models.CharField(max_length=50, blank=True, default='')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='%(app_label)s_%(class)s_sub_uom_categories')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_by_order_filter')
    updated_by = models.ForeignKey(User, related_name='updated_by_order_filter')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % self.name
