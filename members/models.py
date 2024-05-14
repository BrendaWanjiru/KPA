from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

class Member(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=15)
    