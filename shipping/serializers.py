from django.contrib.auth.models import User
from rest_framework import serializers
from shipping.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for ShippingAccount
    """
    class Meta:
        model = Account
        fields = ('id', 'name', 'number', 'address', 'city', 'company', 'country', 'email', 'full_name', 'phone', 'postal', 'state', 'vendor')
