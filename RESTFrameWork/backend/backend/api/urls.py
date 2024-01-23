from django.urls import path
from .views import hello,view_all

urlpatterns = [
     path('',hello),
     path('view_api/<int:my_id>',view_all)
]
