from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from users.forms import LoginUserForm

class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация", 'form': form_class}

    def get_success_url(self):
        return reverse_lazy('main_url') # перенаправляет на имя по адрессу ПРОверьте setting.py

class LogoutUser(LogoutView):
    next_page = reverse_lazy('main_url')