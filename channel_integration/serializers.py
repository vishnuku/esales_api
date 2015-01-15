__author__ = 'vishnu'

from rest_framework import serializers
from .models import ChannelIntegration

class ChannelIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelIntegration
        fields = ('name','site','merchant_id','marketplace_id','merchant_name','status')