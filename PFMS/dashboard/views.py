from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum
import calendar
from expense.models import Expense_Record,Expense_Category
from income.models import Income_Record
from BAM.models import Accounts


@login_required
def dashboard_view(request):
    c = [['category', 'amount']]
    line_chart_data = [['Month', 'Income', 'expense']]

    
    expense_month_user_filtered_sumed_data = Expense_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user).aggregate(Sum('amount')).get('amount__sum')
    
    last_expense_month_user_filtered_sumed_data = Expense_Record.objects.filter(date__month=datetime.now().month-1, account__user =  request.user).aggregate(Sum('amount')).get('amount__sum')

    income_month_user_filtered_sumed_data = Income_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user).aggregate(Sum('amount')).get('amount__sum')

    last_income_month_user_filtered_sumed_data = Income_Record.objects.filter(date__month=datetime.now().month-1, account__user =  request.user).aggregate(Sum('amount')).get('amount__sum')

    net_worth_user_filtered_sumed_data = Accounts.objects.filter(user =  request.user).aggregate(Sum('account_balance')).get('account_balance__sum')

    if last_expense_month_user_filtered_sumed_data is None:
        last_expense_month_user_filtered_sumed_data = 0
    if last_income_month_user_filtered_sumed_data is None:
        last_income_month_user_filtered_sumed_data = 0


    children1 = Expense_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user.id).prefetch_related('category')

    parents = Expense_Category.objects.filter(expense_record__in=children1).distinct()

    for i in parents:
        m = Expense_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user.id, category = i).prefetch_related('category').aggregate(Sum('amount')).get('amount__sum')

        ii = [i.category, m]
        c.append(ii)
 
    
    
    num = 1
    while num <= 12:
        income =  Income_Record.objects.filter(date__month= num, account__user =  request.user).aggregate(Sum('amount')).get('amount__sum')
        expense = Expense_Record.objects.filter(date__month=num, account__user =  request.user).aggregate(Sum('amount')).get('amount__sum')
        month = calendar.month_name[num]
        if income is None:
            income = 0
        if expense is None:
            expense = 0

        data = [month, income, expense]
        line_chart_data.append(data)
        num += 1

    
    context = {
        'expense_data': expense_month_user_filtered_sumed_data,
        'income_data': income_month_user_filtered_sumed_data,
        'net_worth': net_worth_user_filtered_sumed_data,
        'last_month_expense_data': last_expense_month_user_filtered_sumed_data,
        'last_month_income_data': last_income_month_user_filtered_sumed_data,
        'category': c,
        'line_chart_data': line_chart_data

    }

    return render(request, "dashboard/dashboard_view.html", context)


