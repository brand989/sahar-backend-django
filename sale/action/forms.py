from django import forms
from django.contrib.auth.models import User
from comments.models import Comment


class CommentUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Comment
        fields =['text' ]


class ContactForm(forms.Form):

    name = forms.CharField(
        label="Имя",
        widget=forms.TextInput
    )

    nomber = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput
    )

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea
    )


class PartnersForm(forms.Form):

    company = forms.CharField(
        label="Название компании",
        widget=forms.TextInput
    )
    
    name = forms.CharField(
        label="Имя",
        widget=forms.TextInput
    )

    nomber = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput
    )

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea
    )