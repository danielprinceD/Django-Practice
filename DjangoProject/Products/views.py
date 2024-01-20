from django.shortcuts import render

# Create your views here.
from .forms import ProductForm
from .models import Products

def product_form(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request,'ProductForm.html',context={'form':form})

def list_product(request):
    context={
        "object" : Products.objects.all()
    }
    return render(request,'list.html',context=context)
