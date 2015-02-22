from django.conf.urls import url
import views
from integration.views import ListingProducts

urlpatterns = [
    url(r'^channel/$', views.channels),
    url(r'^channel/(?P<pk>[0-9]+)/$', views.channel),
    url(r'^inventory/(?P<pk>[0-9]+)/$', views.inventory),
    url(r'^sync/(?P<pk>[0-9]+)/$', views.sync),
    url(r'^listing/(?P<chid>[0-9]+)/products/$', ListingProducts.as_view()),
]

