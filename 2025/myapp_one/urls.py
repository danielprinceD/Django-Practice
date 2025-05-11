from django.urls import path
from . import views
urlpatterns = [
    path('say_hello' , views.say_hello ),
    path('say_hello_template' , views.say_hello_with_template)
]