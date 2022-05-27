from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from IncExp.forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.


class MyLoginView(LoginView):
    template_name = "IncExp\login.html"
    next_page = 'dashboard'


class IndexView(TemplateView):
    template_name = "IncExp\index.html"


class RegisterView(CreateView):
    template_name = "IncExp\\register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "IncExp\dashboard.html"
    login_url = 'login'
