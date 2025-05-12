from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    hello_obj = HttpResponse('hello world')
    return hello_obj

def say_hello_with_template(request):
    x = 10 
    return render(request , 'hello.html' ,  {
        'name' : 'Daniel Prince D'
    })