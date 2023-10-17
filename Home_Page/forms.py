from django import forms
from django.contrib.auth.forms import AuthenticationForm
from User_Accounts.models import User


class LogInForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control back-drop text-center'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control back-drop text-center'}))

