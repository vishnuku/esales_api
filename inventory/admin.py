from django.contrib import admin

from .models import ChannelCategory, Category, AmazonOrders, ProductType, Inventory, Product, AmazonProduct, Images, \
ProductListingConfigurator

# Register your models here.

class ChannelCategoryAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'node_path', 'item_type_keyword', 'channel', 'parent')


admin.site.register(ChannelCategory, ChannelCategoryAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(AmazonOrders)
class AmazonOrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(AmazonProduct)
class AmazonProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductListingConfigurator)
class ProductListingConfiguratorAdmin(admin.ModelAdmin):
    pass
#
#
# @admin.register()
# class Admin(admin.ModelAdmin):
#     pass
