"""
URL configuration for Pet_Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('Home_Page/', include('Home_Page.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from User_Accounts.views import create_account
from Product.views import create_product
from Pet_Shop.views import page_not_found, server_error, permission_error, request_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home_Page.urls')),
    path('reg/', create_account, name='create_account_page'),
    path('add_prod/', create_product, name='create_product_page'),

]

handler404 = page_not_found

handler500 = server_error

handler403 = permission_error

handler400 = request_error



