from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path
from User import views

app_name = 'User'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.ProfilePage.as_view(), name='profile'),
    path('register/', views.register_user, name='register'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('password-change/done/', views.password_changed, name='password_changed'),
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),


]