from django import forms
from .models import *
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
            'username': forms.TextInput(attrs={'class': 'sign__input'}),
            'email': forms.TextInput(attrs={'class': 'sign__input'}),
            'password': forms.TextInput(attrs={'class': 'sign__input'}),
        }