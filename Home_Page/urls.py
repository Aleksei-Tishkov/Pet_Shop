from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('home/', home_page)
]