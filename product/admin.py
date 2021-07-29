from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'tax',
        'catalogue_pdf',
        'catalogue_image',
        'technical_features',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'tax',
    )


@admin.register(models.OrganizationProduct)
class OrganizationProductAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
