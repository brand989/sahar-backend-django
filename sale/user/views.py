from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import UserOurRegistration, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Вы успешно зарегистрированы')
            return redirect('user')
            
    else:
        form = UserOurRegistration(initial={'username':' ','password1':' ','password2':' ', 'email':' '})
    return render(request, 'users/registration.html',  {'form': form})
    
def profile(request):
    data = { 
        'title': 'Личный кабинет',
        'profile': Profile.objects.all(),

    }
    return render(request, 'users/profile.html', data)

def user_update(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            profile_form.save()
            messages.success(request, f'Вы успешно изменили Ваши данные')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/user_update.html',  {'form': form, 'profile_form': profile_form  })