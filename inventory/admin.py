from django.contrib import admin

from .models import ChannelCategory

# Register your models here.

class ChannelCategoryAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'node_path', 'item_type_keyword', 'channel', 'parent')


admin.site.register(ChannelCategory, ChannelCategoryAdmin)
