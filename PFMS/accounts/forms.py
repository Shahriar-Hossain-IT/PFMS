from django.forms import ModelForm
from django import forms
from .models import Accounts,InterAccountTransaction


class AddNewAccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ('account_name','account_no', 'custodial_name','account_balance', 'opening_date')

        widgets = {
            'account_name': forms.TextInput(attrs={'class':'form-control '}),
            'account_no': forms.NumberInput(attrs={'class':'form-control'}),
            'custodial_name': forms.TextInput(attrs={'class':'form-control'}),
            'account_balance': forms.NumberInput(attrs={'class':'form-control'}),
            'opening_date': forms.DateInput(attrs= {'class':'form-control', 'type':'date'})
            
        }


class UpdateAccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ('account_name','account_no', 'custodial_name')

        widgets = {
            'account_name': forms.TextInput(attrs={'class':'form-control '}),
            'account_no': forms.NumberInput(attrs={'class':'form-control'}),
            'custodial_name': forms.TextInput(attrs={'class':'form-control'}),
            
        }


class AddNewInterAccountTransactionRecord(ModelForm):
    class Meta:
        model = InterAccountTransaction
        fields = ('from_account','to_account', 'amount', 'details','date')

        widgets = {
            'from_account': forms.Select(attrs={'class':'form-control '}),
            'to_account': forms.Select(attrs={'class':'form-control '}),
            'amount': forms.NumberInput(attrs={'class':'form-control', 'step': 0.01}),
            'details': forms.TextInput(attrs={'class':'form-control '}),
            'date' : forms.DateInput(attrs= {'class':'form-control', 'type':'date' })
            
        }

    def __init__(self, user, *args, **kwargs):
        super(AddNewInterAccountTransactionRecord, self).__init__(*args, **kwargs)
        self.fields['from_account'].queryset = Accounts.objects.filter(user = user)
        self.fields['to_account'].queryset = Accounts.objects.filter(user = user)