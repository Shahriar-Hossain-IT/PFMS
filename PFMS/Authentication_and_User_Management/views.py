from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from .forms import UserBasicInfoForm, UserMoreInfoForm
from .serializers import UserSerailizer

# Create your views here.

@login_required
def profile_page_view(request):
    user = User.objects.get(pk=request.user.id)
    context = {
        'user':user
    }

    return render(request, "Authentication_and_User_Management/user_profile.html", context)

@login_required
def profile_update_page_view(request):
    user = User.objects.get(pk=request.user.id)
    basic_info_form = UserBasicInfoForm(request.POST or None, instance=user)
    more_info_form = UserMoreInfoForm(request.POST,request.FILES, instance=user)
    if basic_info_form.is_valid() and more_info_form.is_valid():
        basic_info_form.save()
        more_info_form.save()
        return redirect('profile-page-url')
    context = {
        "basic_info_form": basic_info_form,
        "more_info_form" : more_info_form
    }
    return render(request, "Authentication_and_User_Management/user_profile_update.html", context)


def userSettings(request):
	user = User.objects.get(id=request.user.id)
	setting = user.profile

	seralizer = UserSerailizer(setting, many=False)

	return JsonResponse(seralizer.data, safe=False)


def updateTheme(request):
	data = json.loads(request.body)
	theme = data['theme']
	
	user = User.objects.get(id=request.user.id)
	user.profile.theme_value = theme
	user.profile.save()
	print('Request:', theme)
	return JsonResponse('Updated..', safe=False)