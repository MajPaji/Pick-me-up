from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholder for product type field
        """
        super().__init__(*args, **kwargs)
        self.fields['prtype'].widget.attrs['placeholder'] = 'coffee or cocoa'
