from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import *


# модельки для "пользователя"
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {'username': 'Имя пользователя',
                  'password': 'Пароль',
                  'email': '"E-mail"'}


class AuthorizeForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': 'Имя пользователя', 'password': 'Пароль'}
# конец пользовательских моделек


# начало: формы для книг
class AddBook(forms.Form):
    Author = forms.ChoiceField(widget=forms.Select, choices=Author.objects.all())
    Name = forms.CharField(max_length=30,label='Введите название товара')
    Price = forms.IntegerField(label='Введите цену')


class GetAdditionalInfo(forms.Form):
    Id = forms.IntegerField(label='Введите идентификатор')


class DeleteProduct(forms.Form):
    Name = forms.CharField(max_length=30,label='Введите название товара')


class UpdateProduct(forms.Form):
    Name = forms.CharField(max_length=30,label='Введите название товара')
    NewPrice = forms.IntegerField(label='Введите новую цену')
# конец форм для книг