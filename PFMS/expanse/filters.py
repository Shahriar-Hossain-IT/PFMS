import django_filters
from django_filters import filters
from accounts.models import Accounts
from .models import Expanse_Record, Expanse_Category


def account(request):
    return Accounts.objects.filter(user = request.user)

def category(request):
    return Expanse_Category.objects.filter(user = request.user)


class ExpanseRecordFilter( django_filters.FilterSet):
    account = filters.ModelChoiceFilter(
        queryset=account)
    category = filters.ModelChoiceFilter(
        queryset=category)

    date = filters.DateRangeFilter()
    ammount = filters.RangeFilter()

    class Meta:
        model = Expanse_Record
        fields = '__all__'
        exclude = ['details', 'time']

    
        

        