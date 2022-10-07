from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-mail'

    }))

    password= forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'

    }))



class SignupForm(UserCreationForm):
    name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':' Name'

    }))
    surname=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Surname'

    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'

    }))
    password= forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'

    }))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm Password'

    }))

    class Meta:
        model=User
        fields=['name','surname','email','password1','password2']

    


