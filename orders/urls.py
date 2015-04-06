from django.conf.urls import url
import views


urlpatterns = [
    url(r'^orders/$', views.OrderList.as_view(), name="inventory_orders"),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetails.as_view(), name='inventory_order'),
]
