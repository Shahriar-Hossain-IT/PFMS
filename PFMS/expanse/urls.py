from django.urls import path
from .views import add_new_expanse_record_form, ExpanseCategoryList, ExpanseRecordList, add_new_expanse_category, update_expanse_category, update_expanse_record_form

urlpatterns = [
    path('add-expense-record/', add_new_expanse_record_form, name='add-expanse-record'),
    path('expense-category-list/', ExpanseCategoryList.as_view(), name='expanse-category-list'),
    path('expense-record-list/', ExpanseRecordList.as_view(), name='expanse-record-list'),
    path('add-expense-category/', add_new_expanse_category, name='add-expanse-category'),
    path('update-expense-record/<int:pk>/', update_expanse_record_form , name='update-expanse-record'),
    path('update-expense-category/<int:pk>/', update_expanse_category , name='update-expanse-category'),
]