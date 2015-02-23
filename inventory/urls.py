from django.conf.urls import url
import views

urlpatterns = [
    url(r'^inventory/categories/$', views.CategoryList.as_view(), name="inventory_categories"),
    url(r'^inventory/category/(?P<pk>[0-9]+)/$', views.CategoryDetails.as_view(), name='inventory_category'),
    url(r'^inventory/products/$', views.ProductList.as_view(), name="inventory_products"),
    url(r'^inventory/product/(?P<pk>[0-9]+)/$', views.ProductDetails.as_view(), name='inventory_product'),
    url(r'^inventory/images/$', views.ProductImageList.as_view(), name="inventory_images"),
    url(r'^inventory/image/(?P<pk>[0-9]+)/$', views.ProductImageDetails.as_view(), name='inventory_image'),
    url(r'^inventory/product/images/$', views.ProductWithImagesList.as_view(), name="inventory_product_images"),
    url(r'^inventory/product/image/(?P<pk>[0-9]+)/$', views.ProductWithImagesDetails.as_view(), name='inventory_product_image'),
    url(r'^inventory/csv/$', views.InventoryProductsViaCSV.as_view(), name='inventory_csv')
]
