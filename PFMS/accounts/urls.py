from django.urls import path
from .views import add_new_account_form_view, AccountBalance, AccountTransaction, update_account_form_view

urlpatterns = [
    path('add-new-account/', add_new_account_form_view, name='addnewaccount'),
    path('account-list/', AccountBalance.as_view() , name='account-list'),
    path('transaction-history/', AccountTransaction.as_view() , name='transaction-history'),
    path('update-account/<int:pk>/', update_account_form_view , name='update-account'),
]