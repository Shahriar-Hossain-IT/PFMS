from django.forms import ModelForm
from django import forms
from .models import Expanse_Record, Expanse_Category
from accounts.models import Accounts

class AddNewExpanseRecord(ModelForm):
    class Meta:
        model = Expanse_Record
        fields = ('account','category', 'ammount', 'details','date')

        widgets = {
            'account': forms.Select(attrs={'class':'form-control '}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'ammount': forms.NumberInput(attrs={'class':'form-control'}),
            'details': forms.TextInput(attrs={'class':'form-control '}),
            'date' : forms.DateInput(attrs= {'class':'form-control', 'type':'date' })
            
        }

    def __init__(self, user, *args, **kwargs):
        super(AddNewExpanseRecord, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Accounts.objects.filter(user = user)
        self.fields['category'].queryset = Expanse_Category.objects.filter(user = user)


class AddNewExpanseCategory(ModelForm):
    class Meta:
        model = Expanse_Category
        fields = ('category',)

        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
            
        }


class UpdateExpanseCategory(ModelForm):
    class Meta:
        model = Expanse_Category
        fields = ('category',)

        widgets = {
            'category': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class UpdateExpanseRecord(ModelForm):
    class Meta:
        model = Expanse_Record
        fields = ('account','category', 'ammount', 'details')

        widgets = {
            'account': forms.Select(attrs={'class':'form-control '}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'ammount': forms.NumberInput(attrs={'class':'form-control'}),
            'details': forms.TextInput(attrs={'class':'form-control '})
            
        }

     
    def __init__(self, user, *args, **kwargs):
        super(UpdateExpanseRecord, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Accounts.objects.filter(user = user)
        self.fields['category'].queryset = Expanse_Category.objects.filter(user = user)
    
        