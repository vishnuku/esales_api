from django.conf.urls import url
import receivers
import views


urlpatterns = [
    url(r'^inventory/categories/$', views.CategoryList.as_view(), name="inventory_categories"),
    url(r'^inventory/category/(?P<pk>[0-9]+)/$', views.CategoryDetails.as_view(), name='inventory_category'),
    url(r'^inventory/inventories/$', views.InventoryList.as_view(), name="inventory_inventorys"),
    url(r'^inventory/inventory/(?P<pk>[0-9]+)/$', views.InventoryDetails.as_view(), name='inventory_inventory'),
    url(r'^inventory/products/$', views.ProductList.as_view(), name="inventory_products"),
    url(r'^inventory/product/(?P<pk>[0-9]+)/$', views.ProductDetails.as_view(), name='inventory_product'),
    url(r'^inventory/images/$', views.ProductImageList.as_view(), name="inventory_images"),
    url(r'^inventory/image/(?P<pk>[0-9]+)/$', views.ProductImageDetails.as_view(), name='inventory_image'),
    url(r'^inventory/product/images/$', views.ProductWithImagesList.as_view(), name="inventory_product_images"),
    url(r'^inventory/product/image/(?P<pk>[0-9]+)/$', views.ProductWithImagesDetails.as_view(), name='inventory_product_image'),
    url(r'^inventory/csv/$', views.InventoryProductsViaCSV.as_view(), name='inventory_csv'),
    url(r'^inventory/channel/categories/(?P<channel>[a-zA-Z]+)/(?P<level>[0-9]+)/$', views.ChannelCategoryList.as_view(), name="inventory_channel_categories"),
    url(r'^inventory/channel/categories/(?P<channel>[a-zA-Z]+)/(?P<level>[0-9]+)/(?P<catid>[0-9]+)/$', views.ChannelCategoryList.as_view(), name="inventory_channel_categories"),
    url(r'^inventory/channel/category/(?P<pk>[0-9]+)/$', views.CategoryDetails.as_view(), name='inventory_channel_category'),
    url(r'^inventory/product/configs/$', views.ProductListingConfiguratorList.as_view(), name="inventory_product_listing_configurator"),
    url(r'^inventory/product/config/(?P<pk>[0-9]+)/$', views.ProductListingConfiguratorDetails.as_view(), name='inventory_product_listing_configurators'),
    url(r'^inventory/warehouses/$', views.WarehouseList.as_view(), name="inventory_warehouse"),
    url(r'^inventory/warehouse/(?P<pk>[0-9]+)/$', views.WarehouseDetails.as_view(), name='inventory_warehouse'),
    url(r'^inventory/warehouse/bins/$', views.WarehouseBinList.as_view(), name="inventory_warehouse_product"),
    url(r'^inventory/warehouse/bins/warehouse/(?P<warehouse>[0-9]+)/$', views.WarehouseBinList.as_view(), name='inventory_warehouse_product'),
    url(r'^inventory/warehouse/bins/warehouse/(?P<warehouse>[0-9]+)/(?P<product>[0-1]+)/$', views.WarehouseBinList.as_view(), name='inventory_warehouse_product'),
    url(r'^inventory/warehouse/bins/product/(?P<product>[0-9]+)/$', views.WarehouseBinList.as_view(), name='inventory_warehouse_product'),
    url(r'^inventory/warehouse/bin/(?P<pk>[0-9]+)/$', views.WarehouseBinDetails.as_view(), name='inventory_warehouse_product'),
    url(r'^inventory/product/orders/$', views.ProductOrderList.as_view(), name='inventory_product_order'),
    url(r'^inventory/product/order/(?P<pk>[0-9]+)/$', views.ProductOrderDetails.as_view(), name='inventory_product_order'),
    url(r'^inventory/product/order/order/(?P<order>[0-9]+)/$', views.ProductOrderList.as_view(), name='inventory_warehouse_product'),
    #url(r'^inventory/product/order/order2/(?P<pk>[0-9]+)/$', views.OrderProductDetails.as_view(), name='inventory_order_product_details'),
    url(r'^inventory/bundles/$', views.BundleProductList.as_view(), name='inventory_bundle_products'),
    url(r'^inventory/bundle/(?P<pk>[0-9]+)/$', views.BundleProductDetails.as_view(), name='inventory_bundle_product'),
    url(r'^inventory/bundle/product/(?P<product>[0-9]+)/$', views.BundleProductList.as_view(), name='inventory_bundle_product_product'),

]
