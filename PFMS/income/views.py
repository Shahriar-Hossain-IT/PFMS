from django.shortcuts import render, redirect
from django.views.generic.list import ListView
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import IncomeRecordFilter

##
from .models import Income_Record, Income_Category
from .forms import IncomeRecordForm, IncomeCategoryForm
from BAM.models import Accounts


# Create your views here.
@login_required
def add_income_record_view(request):
    user = request.user
    form = IncomeRecordForm(user, request.POST or None)
    if form.is_valid():
        account = Accounts.objects.get(pk=form.data['account'])
        account.account_balance = account.account_balance + float(form.data['amount'])
        account.last_update_date = datetime.datetime.now()
        account.save()
        form.save()
        form = IncomeRecordForm(user)
    context = {
        'form': form
    }
    return render(request, "income/income_form.html", context)

@login_required
def add_income_category_view(request):
    form = IncomeCategoryForm(request.POST or None)
    if form.is_valid():
        Income_Category = form.save(commit=False) 
        Income_Category.user = request.user
        Income_Category.save() 
        return redirect('income-category-list')
        
    context = {
        'form': form
    }
    return render(request, "income/income_form.html", context)


@login_required
def update_income_category_view(request,pk):
    category=Income_Category.objects.get(pk=pk)
    form = IncomeCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save() 
        return redirect('income-category-list')
        #form.save()
        
    context = {
        'form': form
    }
    return render(request, "income/income_form.html", context)

@login_required
def update_income_record_view(request,pk):
    record = Income_Record.objects.get(pk=pk)
    user = request.user
    form = IncomeRecordForm(user, request.POST or None, instance=record )
    if form.is_valid():
        form.save()
        return redirect('income-record-list')
    context = {
        'form': form
    }
    return render(request, "income/income_form.html", context)


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
        context['form'] = IncomeRecordFilter(self.request.GET,request=self.request, queryset= context['object_list'].select_related('category').order_by('-date'))
        context['object_list'] = context['form'].qs
        return context
