from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm

from User.services import check_email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control back-drop text-center',
                                                             'placeholder': 'Username'}))
    #email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control back-drop'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                 'placeholder': 'Password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control back-drop text-center',
                                                             'placeholder': 'Username'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control back-drop text-center',
                                                            'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                  'placeholder': 'Invent a strong password'}))
    password2 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                  'placeholder': 'Repeat your password'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        # labels = {'first_name': 'What is your first name?', 'last_name': 'What is your last name?'}

    def clean_email(self):
        return check_email(self.cleaned_data['email'])


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Old password',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                     'placeholder': 'Old password'}))
    new_password1 = forms.CharField(label='New password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                      'placeholder': 'Invent a strong password'}))
    new_password2 = forms.CharField(label='New password repeat',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control back-drop text-center',
                                                                      'placeholder': 'Repeat your new password'}))


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control back-drop text-center',
                                                                     'placeholder': 'Enter your e-mail'}))


class UserPasswordResetCompleteForm():
    pass