from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.

class CustomLoginView(LoginView):
    template_name = "userauth/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard')