from django.shortcuts import render
from .models import Expanse_Record, Expanse_Category
from .forms import AddNewExpanseRecord, AddNewExpanseCategory
from accounts.models import Account_Transaction, Accounts
from django.views.generic.list import ListView
import datetime
from django.shortcuts import redirect

# Create your views here.

def add_new_expanse_record_form(request):
    form = AddNewExpanseRecord(request.POST or None)
    if form.is_valid():
        form.save()
        expanse_record = Account_Transaction.objects.create(account_transaction_type='D', account=form.instance.account, ammount=form.data['ammount'],transaction_summary=form.data['details'])

        account = Accounts.objects.get(pk=form.data['account'])
        account.account_balance = account.account_balance - float(form.data['ammount'])
        account.last_update_date = datetime.datetime.now()
        account.save()
        # print(account.account_balance)
        form = AddNewExpanseRecord()
        
    context = {
        'form': form
    }
    return render(request, "expanse/add-expanse-record.html", context)



class ExpanseCategoryList(ListView):
    model = Expanse_Category

class ExpanseRecordList(ListView):
    model = Expanse_Record


def add_new_expanse_category(request):
    form = AddNewExpanseCategory(request.POST or None)
    if form.is_valid():
        form.save()
        # form = AddNewExpanseCategory()
        return redirect('/expanse/expanse-category-list/')
        
    context = {
        'form': form
    }
    return render(request, "expanse/add-expanse-category.html", context)
