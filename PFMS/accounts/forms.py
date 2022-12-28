from django.forms import ModelForm
from django import forms
from .models import Accounts


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