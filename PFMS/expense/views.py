from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
##
from.filters import ExpenseRecordFilter
from .models import Expense_Record, Expense_Category
from .forms import ExpenseRecordForm, ExpenseCategoryForm
from BAM.models import Accounts

# Create your views here.
@login_required
def add_expense_record_view(request):
    user = request.user
    form = ExpenseRecordForm(user, request.POST or None)
    if form.is_valid():
        account = Accounts.objects.get(pk=form.data['account'])
        account.account_balance = account.account_balance - float(form.data['amount'])
        account.last_update_date = datetime.datetime.now()
        account.save()
        form.save()
        form = ExpenseRecordForm(user)
        
    context = {
        'form': form
    }
    return render(request, "expense/expense_form.html", context)

@login_required
def add_expense_category_view(request):
    form = ExpenseCategoryForm(request.POST or None)
    if form.is_valid():
        Expanse_Category = form.save(commit=False) 
        Expanse_Category.user = request.user
        Expanse_Category.save() 
        return redirect('expanse-category-list')
        
    context = {
        'form': form
    }
    return render(request, "expense/expense_form.html", context)

@login_required
def update_expanse_category_view(request,pk):
    category=Expense_Category.objects.get(pk=pk)
    form = ExpenseCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save() 
        return redirect('expanse-category-list')
        
    context = {
        'form': form
    }
    return render(request, "expense/expense_form.html", context)

@login_required
def update_expanse_record_view(request,pk):
    record = Expense_Record.objects.get(pk=pk)
    user = request.user
    form = ExpenseRecordForm(user, request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('expanse-record-list')
        
    context = {
        'form': form
    }
    return render(request, "expense/expense_form.html", context)


class ExpanseCategoryList(LoginRequiredMixin,ListView):
    model = Expense_Category
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user =  self.request.user)
        return context

class ExpanseRecordList(LoginRequiredMixin,ListView):
    model = Expense_Record

    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(account__user =  self.request.user)
        context['form'] = ExpenseRecordFilter(self.request.GET,request=self.request, queryset= context['object_list'].select_related('category').order_by('-date'))
        context['object_list'] = context['form'].qs
        return context