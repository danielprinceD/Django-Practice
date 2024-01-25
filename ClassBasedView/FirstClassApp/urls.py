from django.urls import path
from .views import StudentList
urlpatterns = [
    path('ListClass',StudentList.as_view())
]
