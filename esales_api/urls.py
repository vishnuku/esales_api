from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import obtain_auth_token



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
from rest_framework_bulk.routes import BulkRouter
router = BulkRouter()

router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('integration.urls')),
    url(r'^', include('inventory.urls')),
    url(r'^', include('orders.urls')),
    url(r'^', include('shipping.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
    # url(r'^', include('channel_integration.urls')),
    # url(r'^', include('inventory_management.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)