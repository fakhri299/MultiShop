from django.db import models

# Create your models here.

class Signin(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)



class Signup(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password1=models.CharField(max_length=100)
    passwsord2=models.CharField(max_length=100)