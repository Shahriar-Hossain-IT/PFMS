from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
##
from.filters import ExpanseRecordFilter
from .models import Expanse_Record, Expanse_Category
from .forms import AddNewExpanseRecord, AddNewExpanseCategory, UpdateExpanseCategory, UpdateExpanseRecord
from accounts.models import AccountTransaction, Accounts

# Create your views here.
@login_required
def add_new_expanse_record_form(request):
    user = request.user
    form = AddNewExpanseRecord(user, request.POST or None)
    if form.is_valid():
        form.save()
        expanse_record = AccountTransaction.objects.create(account_transaction_type='D', account=form.instance.account, ammount=form.data['ammount'],transaction_summary=form.data['details'])

        account = Accounts.objects.get(pk=form.data['account'])
        account.account_balance = account.account_balance - float(form.data['ammount'])
        account.last_update_date = datetime.datetime.now()
        account.save()
        form = AddNewExpanseRecord(user)
        
    context = {
        'form': form
    }
    return render(request, "expanse/add-expanse-record.html", context)



class ExpanseCategoryList(LoginRequiredMixin,ListView):
    model = Expanse_Category
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user =  self.request.user)
        return context

class ExpanseRecordList(LoginRequiredMixin,ListView):
    model = Expanse_Record

    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(account__user =  self.request.user)
        context['form'] = ExpanseRecordFilter(self.request.GET,request=self.request, queryset= context['object_list'].select_related('category').order_by('-date'))
        context['object_list'] = context['form'].qs
        return context

@login_required
def add_new_expanse_category(request):
    form = AddNewExpanseCategory(request.POST or None)
    if form.is_valid():
        Expanse_Category = form.save(commit=False) 
        Expanse_Category.user = request.user
        Expanse_Category.save() 
        return redirect('expanse-category-list')
        
    context = {
        'form': form
    }
    return render(request, "expanse/add-expanse-category.html", context)

@login_required
def update_expanse_category(request,pk):
    category=Expanse_Category.objects.get(pk=pk)
    form = UpdateExpanseCategory(request.POST or None, instance=category)
    if form.is_valid():
        form.save() 
        return redirect('expanse-category-list')
        
    context = {
        'form': form
    }
    return render(request, "expanse/add-expanse-category.html", context)

@login_required
def update_expanse_record_form(request,pk):
    record = Expanse_Record.objects.get(pk=pk)
    user = request.user
    form = UpdateExpanseRecord(user, request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('expanse-record-list')
        
    context = {
        'form': form
    }
    return render(request, "expanse/add-expanse-record.html", context)