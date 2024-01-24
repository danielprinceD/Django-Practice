from django.urls import path
from .views import login,register
urlpatterns = [
     path('Login',login),
     path('Register',register)
]
