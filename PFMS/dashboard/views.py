from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum
import calendar
from expanse.models import Expanse_Record,Expanse_Category
from income.models import Income_Record
from accounts.models import Accounts


@login_required
def dashboard_view(request):
    c = [['category', 'ammount']]
    line_chart_data = [['Month', 'Income', 'Expanse']]

    
    expanse_month_user_filtered_sumed_data = Expanse_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user).aggregate(Sum('ammount')).get('ammount__sum')
    
    last_expanse_month_user_filtered_sumed_data = Expanse_Record.objects.filter(date__month=datetime.now().month-1, account__user =  request.user).aggregate(Sum('ammount')).get('ammount__sum')

    income_month_user_filtered_sumed_data = Income_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user).aggregate(Sum('ammount')).get('ammount__sum')

    last_income_month_user_filtered_sumed_data = Income_Record.objects.filter(date__month=datetime.now().month-1, account__user =  request.user).aggregate(Sum('ammount')).get('ammount__sum')

    net_worth_user_filtered_sumed_data = Accounts.objects.filter(user =  request.user).aggregate(Sum('account_balance')).get('account_balance__sum')

    if last_expanse_month_user_filtered_sumed_data is None:
        last_expanse_month_user_filtered_sumed_data = 0
    if last_income_month_user_filtered_sumed_data is None:
        last_income_month_user_filtered_sumed_data = 0


    children1 = Expanse_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user.id).prefetch_related('category')

    parents = Expanse_Category.objects.filter(expanse_record__in=children1).distinct()

    for i in parents:
        m = Expanse_Record.objects.filter(date__month=datetime.now().month, account__user =  request.user.id, category = i).prefetch_related('category').aggregate(Sum('ammount')).get('ammount__sum')

        ii = [i.category, m]
        c.append(ii)
 
    
    
    num = 1
    while num <= 12:
        income =  Income_Record.objects.filter(date__month= num, account__user =  request.user).aggregate(Sum('ammount')).get('ammount__sum')
        expanse = Expanse_Record.objects.filter(date__month=num, account__user =  request.user).aggregate(Sum('ammount')).get('ammount__sum')
        month = calendar.month_name[num]
        if income is None:
            income = 0
        if expanse is None:
            expanse = 0

        data = [month, income, expanse]
        line_chart_data.append(data)
        num += 1

    
    context = {
        'expanse_data': expanse_month_user_filtered_sumed_data,
        'income_data': income_month_user_filtered_sumed_data,
        'net_worth': net_worth_user_filtered_sumed_data,
        'last_month_expanse_data': last_expanse_month_user_filtered_sumed_data,
        'last_month_income_data': last_income_month_user_filtered_sumed_data,
        'category': c,
        'line_chart_data': line_chart_data

    }

    return render(request, "dashboard/dashboard_view.html", context)



