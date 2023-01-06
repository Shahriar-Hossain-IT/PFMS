from django.urls import path
from .views import profile_page_view , profile_update_page_view, userSettings, updateTheme

urlpatterns = [
    path('profile/', profile_page_view, name='profile-page-url'),
    path('profile-update/', profile_update_page_view, name='profile-update-page-url'),
    path('user_settings/', userSettings, name="user_settings"),
	path('update_theme/', updateTheme, name="update_theme"),
]