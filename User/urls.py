from django.conf.urls.static import static
from django.urls import path
from User import views

app_name = 'User'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    #path('logout/', views.Logout.as_view(), name='logout'),

]