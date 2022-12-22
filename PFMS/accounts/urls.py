from django.urls import path
from .views import add_new_account_form_view

urlpatterns = [
    path('add-new-account/', add_new_account_form_view, name='addnewaccount'),
]