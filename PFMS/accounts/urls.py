from django.urls import path
from .views import add_new_account_form_view, AccountBalanceList, AccountTransactionList, update_account_form_view, add_new_inter_account_transaction_record_form

urlpatterns = [
    path('add-new-account/', add_new_account_form_view, name='addnewaccount'),
    path('account-list/', AccountBalanceList.as_view() , name='account-list'),
    path('transaction-history/', AccountTransactionList.as_view() , name='transaction-history'),
    path('update-account/<int:pk>/', update_account_form_view , name='update-account'),
    path('transfer/', add_new_inter_account_transaction_record_form , name='inter-account-transaction'),
]