from django.contrib.auth.views import LoginView
from User.forms import UserLoginForm
from django.shortcuts import render


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'User/Login.html'
    extra_context = {'title': 'Log In'}

