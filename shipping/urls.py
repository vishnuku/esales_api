from django.conf.urls import url
import views


urlpatterns = [
    url(r'^shipping/accounts/$', views.AccountList.as_view(), name="shipping_accounts"),
    url(r'^shipping/account/(?P<pk>[0-9]+)/$', views.AccountDetails.as_view(), name='shipping_account'),
    url(r'^shipping/services/$', views.ServiceList.as_view(), name="shipping_services"),
    url(r'^shipping/service/(?P<pk>[0-9]+)/$', views.ServiceDetails.as_view(), name='shipping_service'),
    url(r'^shipping/packagings/$', views.PackagingList.as_view(), name="shipping_packagings"),
    url(r'^shipping/packaging/(?P<pk>[0-9]+)/$', views.PackagingDetails.as_view(), name='shipping_packaging'),
]
