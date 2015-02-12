from django.conf.urls import url
import views

urlpatterns = [
    url(r'^Categories/$', views.categories, name='inventory_categories'),
    url(r'^Category/(?P<pk>[0-9]+)/$', views.category, name='inventory_category'),
    url(r'^InventoryProducts/$', views.products, name='inventory_products'),
    url(r'^InventoryProduct/(?P<pk>[0-9]+)/$', views.product, name='inventory_product'),
    url(r'^InventoryImage/$', views.inventory_images, name="inventory_images"),
    url(r'^InventoryImages/$', views.InventoryProductImage.as_view(), name="inventory_images")

]

