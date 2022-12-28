from django.urls import path
from .views import add_new_income_record_form, CategoryList, IncomeRecordList, add_new_income_category, update_income_category, update_income_record_form

urlpatterns = [
    path('add-income-record/', add_new_income_record_form, name='add-income-record'),
    path('income-category-list/', CategoryList.as_view(), name='category-list'),
    path('income-record-list/', IncomeRecordList.as_view(), name='income-record-list'),
    path('add-income-category/', add_new_income_category, name='add-income-category'),
    path('update-income-record/<int:pk>/', update_income_record_form , name='update-income-record'),
    path('update-income-category/<int:pk>/', update_income_category , name='update-income-category'),
]