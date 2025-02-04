from django import forms
from django.forms import Textarea

from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(

        attrs={
            'class':'from-control',
            'placeholder':'Create Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(

        attrs={
            'class': 'from-control',
            'placeholder': 'Repeat Password'
        }
    ))
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

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(

        attrs={
            'class': 'from-control',
            'placeholder': 'Enter Username'
        }
    ))


    password = forms.CharField(widget=forms.PasswordInput(

        attrs={
            'class': 'from-control',
            'placeholder': 'Create Password'
        }
    ))


class EmailForm(forms.ModelForm):
    email1 = forms.CharField(widget=forms.EmailInput(

        attrs={

            'placeholder': 'Enter Your Email'
        }
    ))












