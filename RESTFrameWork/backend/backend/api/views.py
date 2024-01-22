from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json 
def hello(request):
    query = {}
    
    query['type'] = request.content_type 
    query['server_name'] = "my_server" 
    query['GET'] = dict(request.GET)
    query['request'] = dict(request.body)
    query['headers'] = dict(request.headers)
    return JsonResponse(query)