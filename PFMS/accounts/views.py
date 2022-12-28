from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import TransactionRecordFilter
from .forms import AddNewAccountForm, UpdateAccountForm
from .models import Accounts, Account_Transaction

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


class AccountBalance(LoginRequiredMixin, ListView):
    model = Accounts
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context


class AccountTransaction(LoginRequiredMixin, ListView):
    model = Account_Transaction
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(account__user =  self.request.user)
        context['form'] = TransactionRecordFilter(self.request.GET,request=self.request, queryset= context['object_list'].order_by('-date'))
        context['object_list'] = context['form'].qs
        return context