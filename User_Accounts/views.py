from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from User_Accounts.models import User, UserManager
from User_Accounts.forms import LogInForm, RegisterNewAccountForm


def create_account(request):
    if request.method == 'GET':
        return render(request, 'User_Accounts/create_account.html')
    data = request.POST
    register_form = RegisterNewAccountForm(data)
    register_form.is_valid()
    # messages.success(request, 'Account created successfully')
    User.objects.create_user(username=register_form.cleaned_data.get('username'),
                             email=register_form.cleaned_data.get('email'),
                             password=register_form.cleaned_data.get('password'))
    return render(request, 'User_Accounts/confirm_email.html')


def user_login():
    pass


def user_logout():
    pass
