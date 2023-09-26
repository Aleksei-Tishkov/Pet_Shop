from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from User_Accounts.models import User, UserManager
from User_Accounts.forms import LogInForm, RegisterNewAccountForm


def login_or_create_account(request):
    if request.method == 'GET':
        return render(request, 'User_Accounts/create_account.html')
    data = request.POST
    if 'login_submit' in data:
        log_in_form = LogInForm(data)
        if log_in_form.is_valid():
            return render(request, 'User_Accounts/create_account.html')
    elif 'register_submit' in data:
        register_form = RegisterNewAccountForm(data)
        if register_form.is_valid():
            UserManager.create_user(username=register_form.cleaned_data.get('username_reg'),
                                    email=register_form.cleaned_data.get('email_reg'),
                                    password=register_form.cleaned_data.get('password_reg'))
        else:
            return render(request, 'base.html')
        username = data.get('username')
        email = data.get("email")
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password1, password2 = data.get('password1'), data.get('password2')
        if not username or not first_name or not last_name:
            return render(request, 'reg/reg_other.html', context={'response': 'Please enter your first and last names'})
        elif not email:
            return render(request, 'reg/reg_other.html',
                          context={'response': 'We need to spam someone, provide us your email'})
        elif password1 is None or password2 is None:
            return render(request, 'reg/reg_other.html', context={'response': 'Password?'})
        elif password1 != password2:
            return render(request, 'reg/reg_other.html', context={'response': 'Passwords?'})
        else:
            new_user = User()
            print(email)
            new_user.create_user(username, first_name, last_name, email, password1)
            return render(request, 'reg/reg_other.html', context={'response': 'Congrats! You can add your notes now!'})


def user_login():
    pass


def user_logout():
    pass
