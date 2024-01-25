from django.urls import path
from .views import StudentList,StudentDetail,StudentCreate
urlpatterns = [
    path('ListClass',StudentList.as_view()),
    path('DetailClass/<int:id>',StudentDetail.as_view() , name = "DetailView"),
    path('CreateView',StudentCreate.as_view())
]
