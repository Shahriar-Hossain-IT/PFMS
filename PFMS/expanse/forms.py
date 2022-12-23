from django.forms import ModelForm
from django import forms
from .models import Expanse_Record, Expanse_Category
import datetime


class AddNewExpanseRecord(ModelForm):
    class Meta:
        model = Expanse_Record
        fields = ('account','category', 'ammount', 'details')

        widgets = {
            'account': forms.Select(attrs={'class':'form-control '}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'ammount': forms.NumberInput(attrs={'class':'form-control'}),
            'details': forms.TextInput(attrs={'class':'form-control '})
            
        }


class AddNewExpanseCategory(ModelForm):
    class Meta:
        model = Expanse_Category
        fields = '__all__'

        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
            
        }