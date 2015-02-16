from django.conf.urls import url
import views

urlpatterns = [
    url(r'^Categories/$', views.categories, name='inventory_categories'),
    url(r'^Category/(?P<pk>[0-9]+)/$', views.category, name='inventory_category'),
    url(r'^InventoryProducts/$', views.products, name='inventory_products'),
    url(r'^InventoryProduct/(?P<pk>[0-9]+)/$', views.product, name='inventory_product'),
    url(r'^InventoryImages/$', views.InventoryProductImageList.as_view(), name="inventory_images"),
    url(r'^InventoryImages/(?P<pk>[0-9]+)/$', views.InventoryProductImageDetails.as_view(), name='inventory_images'),
    url(r'^InventoryProductImages/$', views.InventoryProductWithImagesList.as_view(), name="inventory_product_images"),
    url(r'^InventoryProductImage/(?P<pk>[0-9]+)/$', views.InventoryProductWithImagesDetails.as_view(), name='inventory_product_images'),
]

