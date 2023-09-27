from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from User_Accounts.models import User, UserManager
from User_Accounts.forms import LogInForm, RegisterNewAccountForm


def login_or_create_account(request):
    if request.method == 'GET':
        return render(request, 'User_Accounts/create_account.html')
    data = request.POST
    if 'login_submit' in data:
        user = authenticate(request, username=data.get('username'), password=data.get('password'))
        print(user)
        if user is not None:
            login(request, user)
            print('yay')
            return render(request, 'User_Accounts/create_account.html')
        else:
            return render(request, 'User_Accounts/create_account.html')
    elif 'register_submit' in data:
        register_form = RegisterNewAccountForm(data)
        print(register_form.is_valid())
        register_form.is_valid()
            # messages.success(request, 'Account created successfully')
        User.objects.create_user(username=register_form.cleaned_data.get('username'),
                                email=register_form.cleaned_data.get('email'),
                                password=register_form.cleaned_data.get('password'))
        return render(request, 'User_Accounts/create_account.html')


def user_login():
    pass


def user_logout():
    pass
