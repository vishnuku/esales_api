from django.conf.urls import url
import views

urlpatterns = [
    url(r'^categories/$', views.categories, name='inventory_categories'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='inventory_category'),
    url(r'^inventory_products/$', views.products, name='inventory_products'),
    url(r'^inventory_product/(?P<pk>[0-9]+)/$', views.product, name='inventory_product'),
    url(r'^inventory_images/$', views.InventoryProductImageList.as_view(), name="inventory_images"),
    url(r'^inventory_images/(?P<pk>[0-9]+)/$', views.InventoryProductImageDetails.as_view(), name='inventory_images'),
    url(r'^inventory_product_images/$', views.InventoryProductWithImagesList.as_view(), name="inventory_product_images"),
    url(r'^inventory_product_image/(?P<pk>[0-9]+)/$', views.InventoryProductWithImagesDetails.as_view(), name='inventory_product_images'),
]

