from django.urls import path
from .views import hello,view_all

urlpatterns = [
     path('',hello),
     path('view_api',view_all)
]
