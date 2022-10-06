from django import forms
from .models import Product, ProductType, Album, Merch


class AlbumForm(forms.ModelForm):
    """
    Creates an album form
    """
    class Meta:
        model = Album
        exclude = (
            'product_type',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MerchForm(forms.ModelForm):
    """
    Creates a merch form
    """
    class Meta:
        model = Merch
        exclude = (
            'product_type',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sets the product type to merch
        self.initial['product_type'] = 2
