from .models import Products
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =['name','prize']
        
class RawProductForm(forms.Form):
    name = forms.CharField(required=True)
    prize = forms.DecimalField(required=True)