from django.forms import ModelForm
from django import forms
from .models import Income_Record, Income_Category
from accounts.models import Accounts


class AddNewIncomeRecord( ModelForm):
    class Meta:
        model = Income_Record
        fields = ('account','category', 'ammount', 'details', 'date')

        widgets = {
            'account': forms.Select(attrs={'class':'form-control '}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'ammount': forms.NumberInput(attrs={'class':'form-control'}),
            'details': forms.TextInput(attrs={'class':'form-control '}),
            'date' : forms.DateInput(attrs= {'class':'form-control', 'type':'date' })
        }
    # thanks to https://stackoverflow.com/a/68544098
    def __init__(self, user, *args, **kwargs):
        super(AddNewIncomeRecord, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Accounts.objects.filter(user = user)
        self.fields['category'].queryset = Income_Category.objects.filter(user = user)


class AddNewIncomeCategory(ModelForm):
    class Meta:
        model = Income_Category
        fields = ('category',)


        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
            
        }


class UpdateIncomeCategory(ModelForm):
    class Meta:
        model = Income_Category
        fields = ('category',)


        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class UpdateIncomeRecord( ModelForm):
    class Meta:
        model = Income_Record
        fields = ('account','category', 'ammount', 'details')

        widgets = {
            'account': forms.Select(attrs={'class':'form-control '}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'ammount': forms.NumberInput(attrs={'class':'form-control'}),
            'details': forms.TextInput(attrs={'class':'form-control '})
            
        }
    # thanks to https://stackoverflow.com/a/68544098
    def __init__(self, user, *args, **kwargs):
        super(UpdateIncomeRecord, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Accounts.objects.filter(user = user)
        self.fields['category'].queryset = Income_Category.objects.filter(user = user)