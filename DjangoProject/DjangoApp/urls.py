from django.urls import path
from .views import say_hello , say_hello_dynamic
urlpatterns = [
    
    path("hello",say_hello),
    path("hello/dynamic",say_hello_dynamic)
]
