from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page),
    path('home/', home_page)
]