from django.conf.urls import url
#import receivers
import views


urlpatterns = [
    url(r'^inventory/categories/$', views.CategoryList.as_view(), name="inventory_categories"),
]
