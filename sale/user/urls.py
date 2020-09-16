from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews
from django import forms

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('', views.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('pass-reset/',
        authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'),
        name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
        authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset/done/',
        authViews.PasswordResetDoneView.as_view(template_name='users/pass_reset_done.html'),
        name='password_reset_done'),
    path('password_reset_complete/',
        authViews.PasswordResetCompleteView.as_view(template_name='users/pass_reset_complete.html'),
        name='password_reset_complete'),    
    path('user_update/', views.user_update, name='user_update'),
]
