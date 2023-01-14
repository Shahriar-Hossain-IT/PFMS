from django.urls import path
from .views import profile_page_view , userSettings, updateTheme

urlpatterns = [
    path('user_settings/', userSettings, name="user_settings"),
	path('update_theme/', updateTheme, name="update_theme"),
    path('profile/', profile_page_view, name='profile_page_url'),
]