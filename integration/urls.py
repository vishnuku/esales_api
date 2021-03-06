# from django.conf.urls import url
# import views
#
#
# urlpatterns = [
#     url(r'^channel/$', views.channels),
#     url(r'^channel/(?P<pk>[0-9]+)/$', views.channel),
#     # url(r'^inventory/(?P<pk>[0-9]+)/$', views.inventory), # for amazon
#     url(r'^sync/(?P<pk>[0-9]+)/$', views.sync),
# ]

from django.conf.urls import url

import views


urlpatterns = [
    # Usage: This url return the list of all channels.
    # Filter: Use ?mktp=id for filter channel list, based upon the marketplace id.
    url(r'^inventory/channels/$', views.channels, name='channels'),
    url(r'^inventory/channel/(?P<pk>[0-9]+)/$', views.channel, name='channel'),
    # url(r'^channel/$', views.channels, name='cahnnels'),
    url(r'^inventory/amazon/$', views.inventory),
    url(r'^inventory/test/$', views.test),
    url(r'^inventory/amazon/(?P<pk>[0-9]+)/$', views.inventory),
    # url(r'^inventory/sync/(?P<pk>[0-9]+)/$', views.sync),
    url(r'^inventory/sync/(?P<pk>[0-9]+)/$', views.InventorySync.as_view(), name='sync_view'),
    url(r'^order/sync/(?P<pk>[0-9]+)/$', views.OrderSync.as_view(), name='sync_view'),

    url(r'^listing/(?P<chid>[0-9]+)/sync/(?P<synid>[0-9]+)/$', views.sync),
    url(r'^listing/(?P<chid>[0-9]+)/sync/$', views.sync),
    url(r'^listing/(?P<chid>[0-9]+)/products/$', views.ListingProducts.as_view()),
    url(r'^inventory/order/(?P<pk>[0-9]+)/$', views.InventoryOrder.as_view(), name='inventory_order'),
]
