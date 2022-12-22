from django.shortcuts import render
from .forms import AddNewAccountForm
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