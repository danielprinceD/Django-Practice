from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Student
from django.views.generic import(
    ListView,
    DetailView
)
class StudentList(ListView):
    queryset = Student.objects.all()
    
class StudentDetail(DetailView):
    queryset = Student.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student,id = id_)
    
        