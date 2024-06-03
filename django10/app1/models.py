from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    college=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    