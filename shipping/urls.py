from django.conf.urls import url
import views


urlpatterns = [
    url(r'^shipping/accounts/$', views.AccountList.as_view(), name="shipping_accounts"),
    url(r'^shipping/account/(?P<pk>[0-9]+)/$', views.AccountDetails.as_view(), name='shipping_account'),
]
