from django.shortcuts import render
from .forms import AddNewAccountForm
from django.views.generic.list import ListView
from .models import Accounts, Account_Transaction
# Create your views here.


# Create your views here.

def add_new_account_form_view(request):
    form = AddNewAccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddNewAccountForm()
        
    context = {
        'form': form
    }
    return render(request, "accounts/add-new-account-form.html", context)


class AccountBalance(ListView):
    model = Accounts

class AccountTransaction(ListView):
    model = Account_Transaction