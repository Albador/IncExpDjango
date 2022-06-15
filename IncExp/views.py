from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from IncExp.forms import RegistrationForm, BookingForm
from IncExp.models import Booking
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_list'] = Booking.objects.filter(user=self.request.user).order_by('-date')
        context['booking_list_sum'] = Booking.objects.filter(user=self.request.user).aggregate(Sum('value'))
        return context


class CreateBookingView(LoginRequiredMixin, CreateView):
    template_name = "IncExp\\createbooking.html"
    form_class = BookingForm
    success_url = reverse_lazy('dashboard')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBookingView(LoginRequiredMixin, BaseDetailView):
    http_method_names = ['delete']
    model = Booking

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            response = redirect(reverse_lazy('dashboard'))
            response.status_code = 200
            return response
        else:
            raise PermissionDenied()
