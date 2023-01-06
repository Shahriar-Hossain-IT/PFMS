from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserBasicInfoForm(ModelForm):
    class Meta:
        model = User
        fields = {'first_name','last_name', 'email', }

class UserMoreInfoForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = {'user','birth_date','theme_name', 'theme_value', 'upload',}