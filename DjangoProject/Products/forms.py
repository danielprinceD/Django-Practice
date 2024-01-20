from .models import Products
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =['name','prize']