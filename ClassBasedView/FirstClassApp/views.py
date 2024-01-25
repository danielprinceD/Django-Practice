from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

class StudentList(ListView):
    model = Student
