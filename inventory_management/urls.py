from django.conf.urls import url
import views

urlpatterns = [
    url(r'^category/$', views.category, name='category'),
    url(r'^inventory/$', views.Product, name='inventory')
]

