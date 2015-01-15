from django.conf.urls import url
import views

urlpatterns = [
    url(r'^channel_integration/$', views.channels),
    url(r'^channel_integration/(?P<pk>[0-9]+)/$', views.channel),
]

