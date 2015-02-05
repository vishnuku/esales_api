from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=False, unique=True)
    status = models.SmallIntegerField(max_length=1, default=0)
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=False)

    class Meta:
        ordering = ('created',)
