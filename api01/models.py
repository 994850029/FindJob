from django.db import models

# Create your models here.

class Company(models):
    name = models.CharField(max_length=90)
    introduction = models.TextField()
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

class Job(models):
    name = models.CharField(max_length=90)

