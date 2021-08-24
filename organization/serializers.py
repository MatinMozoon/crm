import product.models
from . import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.models.Product
        fields = ['name']


class OrganizationSerializer(serializers.ModelSerializer):
    organization_product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Organization
        exclude = [
            'slug',
        ]
