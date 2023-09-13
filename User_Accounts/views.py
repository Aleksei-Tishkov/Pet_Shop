from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from User_Accounts.models import User


def create_account(request):
    if request.method == 'GET':
        return render(request, 'User_Accounts/create_account.html')
    data = request.POST
    username = data.get('username')
    email = data.get("email")
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password1, password2 = data.get('password1'), data.get('password2')
    if not username or not first_name or not last_name:
        return render(request, 'reg/reg_other.html', context={'response': 'Please enter your first and last names'})
    elif not email:
        return render(request, 'reg/reg_other.html', context={'response': 'We need to spam someone, provide us your email'})
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


