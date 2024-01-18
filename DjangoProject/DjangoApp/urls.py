from django.urls import path
from . import views as djangoApp
urlpatterns = [
    path("hello",djangoApp.say_hello)
]
