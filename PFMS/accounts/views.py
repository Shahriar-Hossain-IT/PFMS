from django.shortcuts import render
from .forms import AddNewAccountForm
from django.views.generic.list import ListView
from .models import Accounts, Account_Transaction
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def add_new_account_form_view(request):
    form = AddNewAccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddNewAccountForm()
        
    context = {
        'form': form
    }
    return render(request, "accounts/add-new-account-form.html", context)


class AccountBalance(LoginRequiredMixin, ListView):
    model = Accounts


class AccountTransaction(LoginRequiredMixin, ListView):
    model = Account_Transaction