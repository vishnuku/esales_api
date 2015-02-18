from django.conf.urls import url
import views

urlpatterns = [
    url(r'^inventory/categories/$', views.categories, name='inventory_categories'),
    url(r'^inventory/category/(?P<pk>[0-9]+)/$', views.category, name='inventory_category'),
    url(r'^inventory/products/$', views.products, name='inventory_products'),
    url(r'^inventory/product/(?P<pk>[0-9]+)/$', views.product, name='inventory_product'),
    url(r'^inventory/images/$', views.InventoryProductImageList.as_view(), name="inventory_images"),
    url(r'^inventory/image/(?P<pk>[0-9]+)/$', views.InventoryProductImageDetails.as_view(), name='inventory_images'),
    url(r'^inventory/product/images/$', views.InventoryProductWithImagesList.as_view(), name="inventory_product_images"),
    url(r'^inventory/product/image/(?P<pk>[0-9]+)/$', views.InventoryProductWithImagesDetails.as_view(), name='inventory_product_images')
]
