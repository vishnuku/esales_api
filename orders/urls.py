from django.conf.urls import url
import views


urlpatterns = [
    url(r'^orders/$', views.OrderList.as_view(), name="inventory_orders"),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetails.as_view(), name='inventory_order'),
    url(r'^order/filters/$', views.FilterList.as_view(), name="order_filters"),
    url(r'^order/filter/(?P<pk>[0-9]+)/$', views.FilterDetails.as_view(), name='order_filter'),
    url(r'^order/shippings/$', views.OrderShippingList.as_view(), name="order_shipping"),
    url(r'^order/shipping/$', views.OrderShippingDetailDetail.as_view(), name="order_shipping"),

]
