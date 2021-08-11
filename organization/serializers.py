from django.contrib.auth import get_user_model

import product.models
from . import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.models.Product
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    # creator = UserSerializer(many=True, read_only=True)
    organization_product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Organization
        exclude = [
            'slug',
        ]
