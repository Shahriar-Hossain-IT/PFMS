from django.urls import path
from .views import dashboard_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', dashboard_view, name='dashboard'),
]