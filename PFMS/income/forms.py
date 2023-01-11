from django.forms import ModelForm
from django import forms
from .models import Income_Record, Income_Category
from BAM.models import Accounts


class IncomeRecordForm( ModelForm):
    class Meta:
        model = Income_Record
        fields = ('account','category', 'amount', 'details', 'date')

        widgets = {'date': forms.DateInput(attrs= {'class':'form-control', 'type':'date'})}

    # thanks to https://stackoverflow.com/a/68544098
    def __init__(self, user, *args, **kwargs):
        super(IncomeRecordForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Accounts.objects.filter(user = user)
        self.fields['category'].queryset = Income_Category.objects.filter(user = user)


class IncomeCategoryForm(ModelForm):
    class Meta:
        model = Income_Category
        fields = ('category',)