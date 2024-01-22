from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
import json 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Product.models import Product
from Product.serializer import ProductSerializer
@api_view(["GET"])
def hello(request):
    query = {}
    instance = Product.objects.all().order_by("?").first()
    if instance:
        serialized_data = ProductSerializer(instance).data
    return Response(serialized_data)

@api_view(["GET"])
def view_all(request):
    all_data_instance = Product.objects.get(id=5)
    if all_data_instance:
        all_serializer = ProductSerializer(all_data_instance).data
    return Response(all_serializer)
        
