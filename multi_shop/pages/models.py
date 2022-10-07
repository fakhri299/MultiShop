from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    subject=models.TextField(blank=True,null=True)
    message=models.TextField(blank=True)

    def __str__(self):
        return self.email
