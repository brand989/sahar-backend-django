from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserOurRegistration(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text= '- Ваш пароль не может быть слишком похож на другую вашу личную информацию.<br>- Ваш пароль должен содержать как минимум 8 символов. <br>- Ваш пароль не может быть часто используемым паролем.<br>- Ваш пароль должен сожержать буквы и цифры')

    class Meta:
        model = User
        fields =['username', 'email','password1', 'password2' ]


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField()
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields =['username', 'email','first_name', 'last_name' ]



class ProfileUpdateForm(forms.ModelForm):
    nomber_phone = forms.CharField(label='Номер телефона')
    nomber_card = forms.CharField(label='Номер карты')
    
    def __init__(self, *args, **kwards):
        super(ProfileUpdateForm,self).__init__(*args, **kwards)
        self.fields['img'].label="Изображение профиля"

    class Meta:
        model = Profile
        fields =['img', 'nomber_phone', 'nomber_card']