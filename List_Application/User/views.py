from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request,'login.html')

def register(requets):
    return render(requets,'register.html')