# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import CreateView, UpdateView

from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class PasswordChangeFormView(UpdateView):
    template_name = 'registration/password_change_form'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('registration/password_change_done')