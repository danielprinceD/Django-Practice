from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json 
from Product.models import Product
def hello(request):
    query = {}
    product = Product.objects.all().order_by("?").first()
    query['prod_name'] = product.name
    query['prod_price'] = product.price
    return JsonResponse(query)