from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request) : 
    return HttpResponse("<h1> HelloWord from Django App</h1>");

