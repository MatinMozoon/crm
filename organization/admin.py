from django.contrib import admin
from . import models

admin.site.site_header = 'پنل مدیریت نرم افزار ارتباط با مشتری'


@admin.register(models.Organization)
class OrganizationProductAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'audience_full_name',
    )
    list_filter = (
        'creator',
    )