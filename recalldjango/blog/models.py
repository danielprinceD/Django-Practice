from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length = 20)
    subject = models.TextField()
    body = models.TextField()
