from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from jsonfield import JSONField


class Filter(MPTTModel):
    name = models.CharField(max_length=20, blank=True, default='', unique=True)
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

    def __unicode__(self):
        return '%s' % self.name
