from django.forms import ModelForm
from.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    
   
       
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email']