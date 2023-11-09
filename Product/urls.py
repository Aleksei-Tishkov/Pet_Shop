from django.urls import path, include
from Product import views

urlpatterns = [
    path('shop/<slug:slug>/', views.product_view, name='post'),

]