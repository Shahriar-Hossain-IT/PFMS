from django.forms import ModelForm
from django import forms
from .models import Accounts, InterAccountTransaction

class DatePickerInput(forms.DateInput):
        input_type = 'date'



class NewAccountsForm(ModelForm):
    class Meta:
        model = Accounts
        exclude = {'user','last_update_date',}

        widgets = {
            'opening_date': forms.DateInput(attrs= {'class':'form-control', 'type':'date'})
        }


class UpdateAccountForm(ModelForm):
    class Meta:
        model = Accounts
        exclude = {'user','last_update_date','account_balance'}


class AddNewInterAccountTransactionRecord(ModelForm):
    class Meta:
        model = InterAccountTransaction
        fields = ('from_account','to_account', 'amount', 'details','date')

        widgets = {
            'date' : forms.DateInput(attrs= {'class':'form-control', 'type':'date'})
            
        }

    def __init__(self, user, *args, **kwargs):
        super(AddNewInterAccountTransactionRecord, self).__init__(*args, **kwargs)
        self.fields['from_account'].queryset = Accounts.objects.filter(user = user)
        self.fields['to_account'].queryset = Accounts.objects.filter(user = user)