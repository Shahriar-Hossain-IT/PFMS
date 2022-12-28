from django.shortcuts import render, redirect
from django.views.generic.list import ListView
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import IncomeRecordFilter

##
from .models import Income_Record, Income_Category
from .forms import AddNewIncomeRecord, AddNewIncomeCategory,UpdateIncomeCategory,UpdateIncomeRecord
from accounts.models import Account_Transaction, Accounts


# Create your views here.
@login_required
def add_new_income_record_form(request):
    user = request.user
    form = AddNewIncomeRecord(user, request.POST or None)
    if form.is_valid():
        form.save()
        income_record = Account_Transaction.objects.create(account_transaction_type='C', account=form.instance.account, ammount=form.data['ammount'],transaction_summary=form.data['details'])

        account = Accounts.objects.get(pk=form.data['account'])
        account.account_balance = account.account_balance + float(form.data['ammount'])
        account.last_update_date = datetime.datetime.now()
        account.save()
        form = AddNewIncomeRecord(user)
        
    context = {
        'form': form
    }
    return render(request, "income/add-income-record.html", context)



class CategoryList(LoginRequiredMixin,ListView):
    model = Income_Category
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user =  self.request.user)
        return context





class IncomeRecordList(LoginRequiredMixin,ListView):
    model = Income_Record

    context_object_name = 'object_list'
    context_object_name = 'form'

    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(account__user =  self.request.user)
        context['form'] = IncomeRecordFilter(self.request.GET,request=self.request, queryset= context['object_list'].order_by('-date'))
        context['object_list'] = context['form'].qs
        return context

@login_required
def add_new_income_category(request):
    form = AddNewIncomeCategory(request.POST or None)
    if form.is_valid():
        Income_Category = form.save(commit=False) 
        Income_Category.user = request.user
        Income_Category.save() 
        return redirect('category-list')
        
    context = {
        'form': form
    }
    return render(request, "income/add-income-category.html", context)


@login_required
def update_income_category(request,pk):
    category=Income_Category.objects.get(pk=pk)
    form = UpdateIncomeCategory(request.POST or None, instance=category)
    if form.is_valid():
        form.save() 
        return redirect('category-list')
        #form.save()
        
    context = {
        'form': form
    }
    return render(request, "income/add-income-category.html", context)

@login_required
def update_income_record_form(request,pk):
    record = Income_Record.objects.get(pk=pk)
    user = request.user
    form = UpdateIncomeRecord(user, request.POST or None, instance=record )
    if form.is_valid():
        form.save()
        return redirect('income-record-list')
        
    context = {
        'form': form
    }
    return render(request, "income/add-income-record.html", context)

