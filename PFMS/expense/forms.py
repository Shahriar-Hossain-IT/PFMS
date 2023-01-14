from django.forms import ModelForm
from django import forms
from .models import Expense_Record, Expense_Category
from BAM.models import Accounts

class ExpenseRecordForm(ModelForm):
    class Meta:
        model = Expense_Record
        fields = ('account','category', 'amount', 'details','date')

        widgets = {'date': forms.DateInput(attrs= {'class':'form-control', 'type':'date'})}

    def __init__(self, user, *args, **kwargs):
        super(ExpenseRecordForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Accounts.objects.filter(user = user, non_expenditure_account=False )
        self.fields['category'].queryset = Expense_Category.objects.filter(user = user)


class ExpenseCategoryForm(ModelForm):
    class Meta:
        model = Expense_Category
        fields = ('category',)

        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
        }
        