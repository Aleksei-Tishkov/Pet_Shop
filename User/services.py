from django import forms
from django.contrib.auth import get_user_model


def save_new_user(form) -> None:
    '''Checks form validity, sets password and saves user'''
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()


def check_email(email):
    if get_user_model().objects.filter(email=email).exists():
        raise forms.ValidationError('This e-mail has already been used for registration')
    return email

