from django.urls import path
from .views import list_product,product_form,raw_product_form,view_product
urlpatterns = [
     path('list',list_product),
     path('form',product_form), 
     path('raw_form',raw_product_form) ,
     path('id/<int:my_id>',view_product)
]
