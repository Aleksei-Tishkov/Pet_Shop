from django.urls import path, include
from Blog import views

urlpatterns = [
    path('blog/add_post/', views.add_post, name='add_post'),
    path('blog/<slug:slug>/', views.post_view, name='post'),

]