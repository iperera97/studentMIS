from .import models
from django import forms
from .models import User as UserModel


class LoginForm(forms.Form):

    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
