from django.shortcuts import render

# Create your views here.

from .models import Products

def list_product(request):
    context={
        "object" : Products.objects.all()
    }
    return render(request,'list.html',context=context)
