from django import forms
from pages.models import Contact

class ContactForm(forms.ModelForm):
    name= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Name'

    }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-mail'

    }))

    subject= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Subject'

    }))

    message=forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Your Message'

    }))


    class Meta():

        model = Contact
        fields=['name','email','subject','message']

