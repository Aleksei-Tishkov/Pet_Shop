
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy, reverse

from User.forms import UserLoginForm, UserRegisterForm, ChangePassword, UserPasswordResetForm
from django.shortcuts import render, redirect

from User.services import save_new_user


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'User/Login.html'
    extra_context = {'title': 'Log In'}

    # def get_success_url(self):
    # return reverse_lazy('home')


def profile_page(request):
    return render(request, 'User/Profile_page.html', {'title': 'Profile page'})


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        save_new_user(form)
        return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'User/Register.html', {'form': form})


class UserPasswordChangeView(PasswordChangeView):
    form_class = ChangePassword
    success_url = reverse_lazy('User:password_changed')
    template_name = 'User/Password_change.html'
    extra_context = {'title': 'Password change'}


def password_changed(request):
    return render(request, 'User/Password_change_success.html')


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'User/Password_reset_form.html'
    email_template_name = 'User/password_reset_email.html'
    extra_context = {'title': 'Password reset'}
    success_url = reverse_lazy('User:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'User/Password_reset_done.html'
    extra_context = {'title': 'Password reset'}


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'User/Password_reset_confirm.html'
    extra_context = {'title': 'Change password'}
    success_url = reverse_lazy('User:password_reset_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'User/Password_change_success.html'
    extra_context = {'title': 'Done!'}
