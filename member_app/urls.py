from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True ), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/edit/', views.UserChangeView.as_view(), name='profile_edit'),
    path('password/change/', views.PasswordChangeView.as_view(), name='password_change'),
]
