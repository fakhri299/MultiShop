import email
from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.TextField(blank=True)
    message=models.TextField()

    def __str__(self):
        return self.email



