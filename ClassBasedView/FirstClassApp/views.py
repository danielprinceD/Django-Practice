from django.shortcuts import render,HttpResponse
from .models import Student
from django.views.generic import ListView

class StudentList(ListView):
    model = Student
        