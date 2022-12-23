from django.urls import path
from .views import add_new_income_record_form, CategoryList, IncomeRecordList, add_new_income_category

urlpatterns = [
    path('add-income-record/', add_new_income_record_form, name='add-income-record'),
    path('category-list/', CategoryList.as_view(), name='category-list'),
    path('income-record-list/', IncomeRecordList.as_view(), name='income-record-list'),
    path('add-income-category/', add_new_income_category, name='add-income-category'),
]