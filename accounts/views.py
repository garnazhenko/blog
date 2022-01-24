from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import generic
from accounts.forms import RegisterUserForm


class RegisterUser(generic.CreateView):
    template_name = 'blog/register.html'
    form_class = RegisterUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUp(LoginView):
    template_name = 'blog/login.html'
    form_class = AuthenticationForm


def logout_user(request):
    logout(request)
    return redirect('login')
