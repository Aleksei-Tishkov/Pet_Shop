from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from Blog.models import Post
from Blog.services import get_published_posts
from Home_Page.services import get_random_instance, get_random_instances
from Shop.services import get_available_products, get_cart_by_user
from User.forms import UserLoginForm


def home_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
    cart = get_cart_by_user(request.user.pk) if request.user.is_authenticated else None
    return render(request, 'Home_Page/Home_Page.html', {'post': get_random_instance(get_published_posts()),
                                                        'form': UserLoginForm,
                                                        'prods': get_random_instances(get_available_products(), 2),
                                                        'prods_2': get_random_instances(get_available_products(), 2),
                                                        'cart': cart,
                                                        })

