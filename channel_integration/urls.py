from django.conf.urls import url
import views

urlpatterns = [
    url(r'^channel/$', views.channels),
    url(r'^channel/(?P<pk>[0-9]+)/$', views.channel),
    url(r'^inventory/(?P<pk>[0-9]+)/$', views.inventory),
]

