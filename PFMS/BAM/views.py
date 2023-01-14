from django.shortcuts import render, redirect
import datetime
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import NewAccountsForm, UpdateAccountForm, AddNewInterAccountTransactionRecord
from .models import Accounts, InterAccountTransaction

@login_required
def add_new_account_form_view(request):
    form = NewAccountsForm(request.POST or None)
    if form.is_valid():
        Accounts = form.save(commit=False) 
        Accounts.user = request.user
        Accounts.save() 
        form = NewAccountsForm()
        
    context = {
        'form': form
    }
    return render(request, "BAM/bam_form.html", context)


@login_required
def update_account_form_view(request,pk):
    account=Accounts.objects.get(pk=pk)
    form = UpdateAccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save() 
        #return redirect('account-list')
        form = UpdateAccountForm()
    context = {
        'form': form
    }
    return render(request, "BAM/bam_form.html", context)

@login_required
def add_new_inter_account_transaction_record_view(request):
    user = request.user
    form = AddNewInterAccountTransactionRecord(user, request.POST or None)
    if form.is_valid():
        from_account = Accounts.objects.get(pk=form.data['from_account'])
        to_account = Accounts.objects.get(pk=form.data['to_account'])
        from_account.account_balance = from_account.account_balance - float(form.data['amount'])
        to_account.account_balance = to_account.account_balance + float(form.data['amount'])
        from_account.last_update_date = datetime.datetime.now()
        to_account.last_update_date = datetime.datetime.now()
        from_account.save()
        to_account.save()
        form.save()
        form = AddNewInterAccountTransactionRecord(user)
        
    context = {
        'form': form
    }
    return render(request, "BAM/bam_form.html", context)


class AccountBalanceListView(LoginRequiredMixin, ListView):
    model = Accounts
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context

