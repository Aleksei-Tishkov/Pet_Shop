from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from Blog.models import Post
from Blog.services import get_published_posts
from Home_Page.services import get_random_instance


def home_page(request):

    return render(request, 'Home_Page/Home_Page.html', {'post': get_random_instance(get_published_posts())})
