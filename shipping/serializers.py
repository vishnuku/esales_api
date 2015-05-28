from django.contrib.auth.models import User
from rest_framework import serializers
from shipping.models import Account, Service, Packaging


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for ShippingAccount
    """
    class Meta:
        model = Account
        fields = ('id', 'name', 'number', 'address', 'city', 'company', 'country', 'email', 'full_name', 'phone', 'postal', 'state', 'vendor')


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Service
    """
    class Meta:
        model = Service
        fields = ('id', 'name', 'account')


class PackagingSerializer(serializers.ModelSerializer):
    """
    Serializer for ShippingPackaging
    """
    class Meta:
        model = Packaging
        fields = ('id', 'name', 'account')
