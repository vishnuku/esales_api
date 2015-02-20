from django.conf.urls import url
import views

urlpatterns = [
    url(r'^inventory/categories/$', views.ProductCategoryList.as_view(), name="inventory_product_categories"),
    url(r'^inventory/category/(?P<pk>[0-9]+)/$', views.ProductCategoryDetails.as_view(), name='inventory_product_category'),
    url(r'^inventory/products/$', views.ProductList.as_view(), name="inventory_products"),
    url(r'^inventory/product/(?P<pk>[0-9]+)/$', views.ProductDetails.as_view(), name='inventory_product'),
    url(r'^inventory/images/$', views.InventoryProductImageList.as_view(), name="inventory_images"),
    url(r'^inventory/image/(?P<pk>[0-9]+)/$', views.InventoryProductImageDetails.as_view(), name='inventory_image'),
    url(r'^inventory/product/images/$', views.InventoryProductWithImagesList.as_view(), name="inventory_product_images"),
    url(r'^inventory/product/image/(?P<pk>[0-9]+)/$', views.InventoryProductWithImagesDetails.as_view(), name='inventory_product_image')
]
