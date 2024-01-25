from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("ListView")
     
    