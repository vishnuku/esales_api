from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import OrderShippingDetail, Filter


@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderShippingDetail)
class OrderShippingDetailAdmin(admin.ModelAdmin):
    pass