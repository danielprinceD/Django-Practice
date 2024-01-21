from django.shortcuts import render
# Create your views here.
from .forms import ProductForm,RawProductForm
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

def raw_product_form(request):
    raw_form = RawProductForm(request.POST or None)
    if raw_form.is_valid():
        Products.objects.create(**raw_form.cleaned_data)
        raw_form = RawProductForm()
    
    return render(request,'raw_form.html',{"raw_form":raw_form})