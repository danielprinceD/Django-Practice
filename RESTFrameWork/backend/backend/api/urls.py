from django.urls import path
from .views import hello,view_all,post_data

urlpatterns = [
     path('',hello),
     path('view_api/<int:my_id>',view_all),
     path("post",post_data)
]
