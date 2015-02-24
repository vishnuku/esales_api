from django.contrib import admin
from .models import AmazonCategories


class AmazonCategoriesAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'node_path', 'item_type_keyword', 'created_by', 'created')


admin.site.register(AmazonCategories, AmazonCategoriesAdmin)
