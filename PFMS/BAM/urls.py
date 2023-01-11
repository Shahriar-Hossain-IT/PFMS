from django.urls import path
from .views import add_new_account_form_view, update_account_form_view, add_new_inter_account_transaction_record_view, AccountBalanceListView
urlpatterns = [
    path('add-new-account/', add_new_account_form_view, name='add_new_account'),
    path('update-account/<int:pk>/', update_account_form_view , name='update_account'),
    path('account-list/', AccountBalanceListView.as_view() , name='account_list'),
    path('transfer/', add_new_inter_account_transaction_record_view , name='inter_account_transaction'),
]