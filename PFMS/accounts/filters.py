import django_filters
from django_filters import filters
from .models import Accounts, AccountTransaction


def account(request):
    return Accounts.objects.filter(user = request.user)



class TransactionRecordFilter( django_filters.FilterSet):
    account = filters.ModelChoiceFilter(
        queryset=account)
    ammount = filters.RangeFilter()
    date = filters.DateRangeFilter()

    class Meta:
        model = AccountTransaction
        fields = '__all__'
        exclude = ['transaction_summary']

    
        

        