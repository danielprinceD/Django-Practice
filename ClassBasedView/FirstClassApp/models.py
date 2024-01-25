from django.db import models

class Student(models.Model):
    name = models.CharField()
    roll = models.IntegerField()