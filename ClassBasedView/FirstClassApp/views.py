from django.shortcuts import render,HttpResponse
from .models import Student
from django.views.generic import(
    ListView,
    DetailView
)
class StudentList(ListView):
    queryset = Student.objects.all()
    
class StudentDetail(DetailView):
    queryset = Student.objects.all()
        