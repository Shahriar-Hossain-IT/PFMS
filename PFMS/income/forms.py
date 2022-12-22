from django.forms import ModelForm
from django import forms
from .models import Income_Record
import datetime


class AddNewIncomeRecord(ModelForm):
    class Meta:
        model = Income_Record
        fields = ('account','category', 'ammount', 'details')

        widgets = {
            'account': forms.Select(attrs={'class':'form-control '}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'ammount': forms.NumberInput(attrs={'class':'form-control'}),
            'details': forms.DateInput(attrs= {'class':'form-control', 'type':'date'})
            
        }