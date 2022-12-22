from django.urls import path
from .views import add_new_income_record_form, CategoryList

urlpatterns = [
    path('add-income-record/', add_new_income_record_form, name='add-income-record'),
    path('Category-List/', CategoryList.as_view(), name='category-list'),
]