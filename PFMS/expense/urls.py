from django.urls import path
from .views import add_expense_record_view, add_expense_category_view,update_expanse_record_view, update_expanse_category_view, ExpanseRecordList, ExpanseCategoryList

urlpatterns = [
    path('add-expense-record/', add_expense_record_view, name='add-expanse-record'),
    path('expense-category-list/', ExpanseCategoryList.as_view(), name='expanse-category-list'),
    path('expense-record-list/', ExpanseRecordList.as_view(), name='expanse-record-list'),
    path('add-expense-category/', add_expense_category_view, name='add-expanse-category'),
    path('update-expense-record/<int:pk>/', update_expanse_record_view , name='update-expanse-record'),
    path('update-expense-category/<int:pk>/', update_expanse_category_view , name='update-expanse-category'),
]