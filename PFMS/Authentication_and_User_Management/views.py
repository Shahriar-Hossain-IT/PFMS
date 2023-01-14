from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from .forms import UserBasicInfoForm, UserMoreInfoForm
from .serializers import UserSerailizer
from datetime import datetime

# Create your views here.

def get_ip_address(request):
        user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip_address:
            ip = user_ip_address.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

@login_required
def profile_page_view(request):
    user = User.objects.get(pk=request.user.id)
    basic_info_form = UserBasicInfoForm(request.POST or None, instance=user)
    more_info_form = UserMoreInfoForm(request.POST or None, instance=user.profile)
    if basic_info_form.is_valid() and more_info_form.is_valid():
        basic_info_form.save()
        more_info_form.save()
        return redirect('profile-page-url')
    context = {
        'user':user,
        'user_ip': get_ip_address(request),
        "basic_info_form": basic_info_form,
        "more_info_form" : more_info_form
    }

    return render(request, "Authentication_and_User_Management/user_profile.html", context)

@login_required
def userSettings(request):
	user = User.objects.get(id=request.user.id)
	setting = user.profile

	seralizer = UserSerailizer(setting, many=False)

	return JsonResponse(seralizer.data, safe=False)

@login_required
def updateTheme(request):
	data = json.loads(request.body)
	theme = data['theme']
	
	user = User.objects.get(id=request.user.id)
	user.profile.theme_value = theme
	user.profile.save()
	print('Request:', theme)
	return JsonResponse('Updated..', safe=False)