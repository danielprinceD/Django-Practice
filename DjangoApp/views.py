from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h2>This is my Home Page<h2>")

def say_hello(request) : 
    return HttpResponse("<h1> HelloWord from Django App</h1>");

def say_hello_dynamic(request):
    return render(request,'template\hello.html',{'name' : 'daniel'})

