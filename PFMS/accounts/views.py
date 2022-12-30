from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime

from .filters import TransactionRecordFilter
from .forms import AddNewAccountForm, UpdateAccountForm, AddNewInterAccountTransactionRecord
from .models import Accounts, AccountTransaction, InterAccountTransaction

# Create your views here.
@login_required
def add_new_account_form_view(request):
    form = AddNewAccountForm(request.POST or None)
    if form.is_valid():
        Accounts = form.save(commit=False) 
        Accounts.user = request.user
        Accounts.save() 
        form = AddNewAccountForm()
        
    context = {
        'form': form
    }
    return render(request, "accounts/add-new-account-form.html", context)

@login_required
def update_account_form_view(request,pk):
    account=Accounts.objects.get(pk=pk)
    form = UpdateAccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save() 
        return redirect('account-list')
        
    context = {
        'form': form
    }
    return render(request, "accounts/add-new-account-form.html", context)


class AccountBalanceList(LoginRequiredMixin, ListView):
    model = Accounts
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context


class AccountTransactionList(LoginRequiredMixin, ListView):
    model = AccountTransaction
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(account__user =  self.request.user)
        context['form'] = TransactionRecordFilter(self.request.GET,request=self.request, queryset= context['object_list'].select_related('account').order_by('-date'))
        context['object_list'] = context['form'].qs.select_related('account')
        return context

@login_required
def add_new_inter_account_transaction_record_form(request):
    user = request.user
    form = AddNewInterAccountTransactionRecord(user, request.POST or None)
    if form.is_valid():
        form.save()
        transaction_record = AccountTransaction.objects.create(account_transaction_type='T', account= form.instance.from_account, ammount=form.data['amount'],transaction_summary={form.data['details']})

        from_account = Accounts.objects.get(pk=form.data['from_account'])
        to_account = Accounts.objects.get(pk=form.data['to_account'])
        from_account.account_balance = from_account.account_balance - float(form.data['amount'])
        to_account.account_balance = to_account.account_balance + float(form.data['amount'])
        from_account.last_update_date = datetime.datetime.now()
        to_account.last_update_date = datetime.datetime.now()
        from_account.save()
        to_account.save()
        form = AddNewInterAccountTransactionRecord(user)
        
    context = {
        'form': form
    }
    return render(request, "accounts/Inter-Account-Transaction-Form.html", context)
