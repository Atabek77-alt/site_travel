from django import forms
from django.forms import Textarea

from .models import Appeal



class ContactForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(

        attrs={
            'class': 'from-control',
            'placeholder': 'Enter Username'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(

        attrs={

            'placeholder': 'Enter Email'
        }
    ))

    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Subject'
        }
    ) )

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Enter message'
        }
    ))

    class Meta:
        model = Appeal
        fields = ['name', 'email', 'subject', 'message']







