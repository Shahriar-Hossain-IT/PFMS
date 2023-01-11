import django_filters
from django_filters import filters
from BAM.models import Accounts
from .models import Income_Record, Income_Category


def account(request):
    return Accounts.objects.filter(user = request.user)

def category(request):
    return Income_Category.objects.filter(user = request.user)


class IncomeRecordFilter( django_filters.FilterSet):
    account = filters.ModelChoiceFilter(
        queryset=account)
    category = filters.ModelChoiceFilter(
        queryset=category)

    date = filters.DateRangeFilter()
    amount = filters.RangeFilter()

    class Meta:
        model = Income_Record
        fields = '__all__'
        exclude = ['details', 'time']

    
        

        