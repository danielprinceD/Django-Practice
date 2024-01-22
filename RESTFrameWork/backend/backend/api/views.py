from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
import json 
from Product.models import Product
def hello(request):
    query = {}
    product = Product.objects.all().order_by("?").first()
    query['prod_name'] = product.name
    query['prod_price'] = product.price
    
    newDate = model_to_dict(product)
    return JsonResponse(newDate)
