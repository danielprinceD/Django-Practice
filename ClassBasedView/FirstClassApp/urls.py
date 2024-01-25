from django.urls import path
from .views import StudentList,StudentDetail
urlpatterns = [
    path('ListClass',StudentList.as_view()),
    path('DetailClass/<int:id>',StudentDetail.as_view())
]
