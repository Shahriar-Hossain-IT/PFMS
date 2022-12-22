from django.shortcuts import render
from .models import Income_Record, Income_Category
from .forms import AddNewIncomeRecord
from accounts.models import Account_Transaction, Accounts
from django.views.generic.list import ListView
import datetime
# Create your views here.

def add_new_income_record_form(request):
    form = AddNewIncomeRecord(request.POST or None)
    if form.is_valid():
        form.save()
        income_record = Account_Transaction.objects.create(account_transaction_type='C', account=form.instance.account, ammount=form.data['ammount'],transaction_summary=form.data['details'])

        account = Accounts.objects.get(pk=form.data['account'])
        account.account_balance = account.account_balance + float(form.data['ammount'])
        account.last_update_date = datetime.datetime.now()
        account.save()
        # print(account.account_balance)
        form = AddNewIncomeRecord()
        
    context = {
        'form': form
    }
    return render(request, "income/add-income-record.html", context)



class CategoryList(ListView):
    model = Income_Category

