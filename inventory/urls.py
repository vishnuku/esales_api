from django.conf.urls import url
import views

urlpatterns = [
    url(r'^inventory/categories/$', views.categories, name='categories'),
    url(r'^inventory/category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^inventory/products/$', views.products, name='inventory_products'),
    url(r'^inventory/product/(?P<pk>[0-9]+)/$', views.product, name='product'),
    url(r'^inventory/images/$', views.ProductImageList.as_view(), name="images"),
    url(r'^inventory/image/(?P<pk>[0-9]+)/$', views.ProductImageDetails.as_view(), name='images'),
    url(r'^inventory/product/images/$', views.ProductWithImagesList.as_view(), name="product_images"),
    url(r'^inventory/product/image/(?P<pk>[0-9]+)/$', views.ProductWithImagesDetails.as_view(), name='product_images'),
]
