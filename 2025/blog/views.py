from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request) :
    return HttpResponse("This is home page")

def blog_details(requst , post_id):
    return HttpResponse(f"Blog details Page {post_id}")

def deprecated_url(request):
    return redirect('new_url_page')

def new_url(request):
    return HttpResponse("This is new url")