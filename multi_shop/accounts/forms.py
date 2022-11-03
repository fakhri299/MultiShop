from django.forms import ModelForm
from accounts.models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

       
