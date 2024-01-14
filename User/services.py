from django import forms
from django.contrib.auth import get_user_model


def save_new_user(form) -> None:
    '''Checks form validity, sets password and saves user'''
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password1'])
    user.save()


def create_theme_entry_for_user(user_theme, user, theme_number=0):
    entry = user_theme.objects.create(user_theme_user=user, user_theme_theme=theme_number)
    entry.save()



def check_email(email):
    if get_user_model().objects.filter(email=email).exists():
        raise forms.ValidationError('This e-mail has already been used for registration')
    return email







