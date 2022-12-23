from django.urls import path
from .views import add_new_expanse_record_form, ExpanseCategoryList, ExpanseRecordList, add_new_expanse_category

urlpatterns = [
    path('add-expanse-record/', add_new_expanse_record_form, name='add-expanse-record'),
    path('expanse-category-List/', ExpanseCategoryList.as_view(), name='expanse-category-list'),
    path('expanse-record-list/', ExpanseRecordList.as_view(), name='expanse-record-list'),
    path('add-expanse-category/', add_new_expanse_category, name='add-expanse-category'),
]