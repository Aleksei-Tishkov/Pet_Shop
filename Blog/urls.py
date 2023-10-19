from django.urls import path, include
from Blog import views

urlpatterns = [
    path('blog/<slug:slug>/', views.post_view, name='post'),

]