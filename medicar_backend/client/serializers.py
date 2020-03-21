from django.contrib.auth.models import User
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    """ Client Serializer"""
    class Meta:
        model = User
        fields = '__all__'