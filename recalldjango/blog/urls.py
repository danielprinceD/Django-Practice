from django.urls import path
from .views import get_user
urlpatterns = [
    path('user' , get_user)
]