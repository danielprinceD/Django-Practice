from django.shortcuts import render , get_object_or_404
from .models import Product
from .serializer import ProductSerializer
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    ListCreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
) 
from .permissions import Staff_Permissions
from rest_framework import mixins , permissions ,authentication
from django.urls import reverse
class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id = id_)
    
class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateAPI(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDestroyAPI(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product,id=id_)

class ProductMixins(mixins.ListModelMixin,
                GenericAPIView,mixins.RetrieveModelMixin,
                mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [Staff_Permissions]
    lookup_field  = 'id'
    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        if id is not None:
             return self.retrieve(request ,*args,**kwargs)
        return self.list(request)
    
    def post(self,request,*args , **kwargs):
        return self.create(request,*args,**kwargs)

product_mixin_generic_view = ProductMixins.as_view()
    