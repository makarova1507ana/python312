from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginUserForm
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import RegisterUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация", 'form': form_class}

    def get_success_url(self):
        return reverse_lazy('main_url') # перенаправляет на имя по адрессу ПРОверьте setting.py


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main_url')


# users/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from .forms import ProfileUserForm


# Класс ProfileUser для отображения и редактирования профиля пользователя
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Используем модель пользователя
    form_class = ProfileUserForm  # Форма профиля пользователя
    template_name = 'profile.html'  # Шаблон для профиля пользователя
    extra_context = {'title': "Профиль пользователя"}# 'default_image': settings.DEFAULT_USER_IMAGE}

    # Метод для получения URL после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy('profile')

    # Метод для получения объекта текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user

