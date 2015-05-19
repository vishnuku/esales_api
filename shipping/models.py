from django.contrib.auth.models import User
from django.db import models

# Create your models here.
SHIPPINGVENDOR = (
    ('USPS', 'USPS'),
)


class Account(models.Model):
    number = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=105, blank=False)
    address = models.CharField(max_length=105, blank=False)
    city = models.CharField(max_length=105, blank=False)
    company = models.CharField(max_length=105, blank=False)
    country = models.CharField(max_length=105, blank=False)
    email = models.CharField(max_length=105, blank=False)
    full_name = models.CharField(max_length=105, blank=False)
    phone = models.CharField(max_length=105, blank=False)
    postal = models.CharField(max_length=105, blank=False)
    state = models.CharField(max_length=105, blank=False)
    vendor = models.CharField(choices=SHIPPINGVENDOR, default=1, max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('name','number',)
