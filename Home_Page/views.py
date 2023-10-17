from aiogram.utils.mixins import DataMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from User_Accounts.models import User, UserManager
from User_Accounts.forms import LogInForm

# Create your views here.


def home_page(request):
    if request.method == 'GET':
        return render(request, 'Home_Page/Home_Page.html')
    data = request.POST
    user = authenticate(request, username=data.get('email'), password=data.get('password'))
    if user is not None:
        login(request, user)
        return render(request, 'Home_Page/Home_Page.html')
    else:
        return render(request, 'Home_Page/Home_Page.html')