from django.urls import path
from .views import list_product,product_form
urlpatterns = [
     path('list',list_product),
     path('form',product_form) 
]
