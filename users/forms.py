from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': "form-control bg-dark text-light",
        'placeholder': "Enter your username"
    }))

    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={
        'class': "form-control bg-dark text-light",
        'placeholder': "Enter your email"
    }))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form-control bg-dark text-light",
        'placeholder': "Enter your password"
    }))


    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form-control bg-dark text-light",
        'placeholder': "Confirm your password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
