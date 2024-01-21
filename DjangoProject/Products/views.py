from django.shortcuts import render,redirect,get_object_or_404
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

def view_product(request,my_id):
    obj = Products.objects.get(id=my_id)
    form = ProductForm( request.POST or None ,  instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request,'product_id.html',{"id":form,"j" : 1})

def delete_product(request,my_id):
    obj = get_object_or_404(Products,id=my_id)
    if request.method=="POST":
        obj.delete()
        return redirect('/product/list')
    return render(request,'delete_id.html',context={"id":obj})