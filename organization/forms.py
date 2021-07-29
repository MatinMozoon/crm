from django import forms
from . import models


class Organization(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = (
            'name',
            'province',
            'phone_number',
            'number_of_employees',
            'organization_product',
            'audience_full_name',
            'audience_phone_number',
            'email',
        )
