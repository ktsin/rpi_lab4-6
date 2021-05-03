from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
import datetime


def index(request):
    return render(request, 'BaseIndex.html')


def about(request):
    return render(request, 'common/about.html')


def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/register.html',{"form" : form})
    else:
        data = {'email' : request.POST.get("email"),
                'name': request.POST.get("username"),
                'password':request.POST.get("password")}
        if User.objects.filter(username=data['name']).exists():
            form = RegisterForm(request.POST)
            form.add_error('username', 'Пользователь с данным логином уже существует')
            return render(request, 'user/register.html', {'form': form,'title':'Регистрация'})
        else:
            User.objects.create_user(data['name'], data['email'], data['password'])
            user = authenticate(request, username=data['name'], password=data['password'])
            login(request, user)
            return redirect('/')


def auth_user(request):
    if not request.user.is_anonymous:
        return redirect('/profile/')
    if request.method == "GET":
        form = AuthorizeForm()
        return render(request, 'user/auth.html',{"form" : form})
    else:
        data = {'name': request.POST.get("username"),
                'password':request.POST.get("password")}
        if not User.objects.filter(username=data['name']).exists():
            form = AuthorizeForm(request.POST)
            form.add_error('username', 'Пользователя с данным именем не существует')
            return render(request, 'user/auth.html', {'form': form, 'title':'Авторизация'})
        else:
            user = authenticate(request,username=data['name'], password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('/profile/')
            else:
                form = AuthorizeForm(request.POST)
                form.errors['username'] = ""
                form.add_error('password', 'Неправильный пароль')
                return render(request, 'user/auth.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


def profile(request):
    if request.method == "GET":
        return render(request,'user/user_details.html',{'title':'Профиль','category': "Выберите категорию"})
    else:
        data = {'name': request.POST.get("productName")}
        products = list(Product.objects.filter(Name__contains=data['name']))
        cols = ['Название', 'Цена', 'Категория']
        rows = []
        for item in products:
            rows.append([item.Name, item.Price,item.Type.TypeName ])
        return render(request,'profile.html',{'cols': cols, 'rows': rows,'category': f"Поиск - {data['name']}"})


def all_books(request):
    if request.method == "GET":
        return render(request, 'book_shop/main_books.html', {'categories' : KnowledgeCategory.objects.all()})
    return None