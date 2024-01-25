from django.urls import path
from .views import StudentList,StudentDetail,StudentCreate,StudentUpdate
urlpatterns = [
    path('ListClass',StudentList.as_view(),name="ListView"),
    path('DetailClass/<int:id>',StudentDetail.as_view() , name = "DetailView"),
    path('CreateView',StudentCreate.as_view()),
    path('<int:id>/UpdateView',StudentUpdate.as_view())
]
