from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control back-drop text-center',
                                                             'placeholder': 'Username',}))
    # email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control back-drop'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                 'placeholder': 'Password'}))
