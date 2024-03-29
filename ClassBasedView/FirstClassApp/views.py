from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Student
from django.urls import reverse
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import StudentForm
class StudentList(ListView):
    queryset = Student.objects.all()
    
class StudentDetail(DetailView):
    queryset = Student.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student,id = id_)
    
class StudentCreate(CreateView):
    form_class = StudentForm
    template_name = 'FirstClassApp/student_create.html'
    querset = Student.objects.all()
    
class StudentUpdate(UpdateView):
    form_class = StudentForm
    template_name = 'FirstClassApp/student_create.html'
    
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student,id=id_)
    
class StudentDelete(DeleteView):
    template_name = 'FirstClassApp/student_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student,id = id_)
    
    def get_success_url(self):
        return reverse("ListView")