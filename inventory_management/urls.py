from django.conf.urls import url
import views

urlpatterns = [
    url(r'^Category/$', views.category, name='category'),
    url(r'^InventoryProducts/$', views.Products, name='inventory_products'),
    url(r'^InventoryProduct/(?P<pk>[0-9]+)/$', views.Product, name='inventory_product')
]

