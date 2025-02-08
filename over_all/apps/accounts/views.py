from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, FormView, DetailView
from .models import  *
from .forms import *


class RegisterView(CreateView):
    model = User
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'pages/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')

        password = form.cleaned_data.get('password')
        user = authenticate(username = username,password=password)

        if user is not None:
            if user.is_active:
                login(self.request,user)
                return  redirect('home')
            else:
                return HttpResponse(' Этот пользователь заблокирован')
        else:
            return HttpResponse(' Такого пользователя не существует или данные неправильны')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')



class SubView(CreateView):
    model = Emails
    template_name = 'templates/base.html'
    form_class = EmailForm


class ProfileView(DetailView):
    template_name = 'pages/profile.html'
    model = User
    context_object_name = 'profile'
    queryset = User.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_id = kwargs.get('pk',self.request.user.pk)
    #     context['user'] = User.objects.get(pk=user_id)
    #     return context
























