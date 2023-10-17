from django import forms
from .models import User


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterNewAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


