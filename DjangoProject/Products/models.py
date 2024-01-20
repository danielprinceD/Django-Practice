from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.TextField()
    prize = models.IntegerField()
