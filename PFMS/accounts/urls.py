from django.urls import path
from .views import add_new_account_form_view, AccountBalance, AccountTransaction

urlpatterns = [
    path('add-new-account/', add_new_account_form_view, name='addnewaccount'),
    path('account-balance/', AccountBalance.as_view() , name='account-balance'),
    path('Transaction-History/', AccountTransaction.as_view() , name='transaction-history'),
]