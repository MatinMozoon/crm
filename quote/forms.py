from django.forms import modelformset_factory, inlineformset_factory

from quote import models


QuoteItemFormSet = inlineformset_factory(
    models.Quote,
    models.QuoteItem,
    fields=('product_name', 'quantity', 'price', 'discount')
)
