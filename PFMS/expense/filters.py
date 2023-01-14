import django_filters
from django_filters import filters
from BAM.models import Accounts
from .models import Expense_Record, Expense_Category


def account(request):
    return Accounts.objects.filter(user = request.user, non_expenditure_account=False)

def category(request):
    return Expense_Category.objects.filter(user = request.user)


class ExpenseRecordFilter( django_filters.FilterSet):
    account = filters.ModelChoiceFilter(
        queryset=account)
    category = filters.ModelChoiceFilter(
        queryset=category)

    date = filters.DateRangeFilter()
    amount = filters.RangeFilter()

    class Meta:
        model = Expense_Record
        fields = '__all__'
        exclude = ['details', 'time']

    
        

        