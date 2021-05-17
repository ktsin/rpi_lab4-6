from django.contrib.auth import authenticate, login, logout, base_user, get_user
from django.contrib.auth import models
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

from .forms import *
from django.http import HttpResponse
import datetime


def isLoggedIn(request):
    usr = get_user(request)
    if usr.is_anonymous:
        return False
    else:
        return True


def index(request):
    return render(request, 'BaseIndex.html')


def about(request):
    userBar = render_to_string('user/user_bar.html', {'isLoggedIn': isLoggedIn(request)})
    return render(request, 'common/about.html', {'user_content': userBar})


def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/register.html', {"form": form})
    else:
        data = {'email': request.POST.get("email"),
                'name': request.POST.get("username"),
                'password': request.POST.get("password")}
        if AdvUser.objects.filter(username=data['name']).exists():
            form = RegisterForm(request.POST)
            form.add_error('username', 'Пользователь с данным логином уже существует')
            return render(request, 'user/register.html', {'form': form, 'title': 'Регистрация'})
        else:
            AdvUser.objects.create_user(data['name'], data['email'], data['password'])
            user = authenticate(request, username=data['name'], password=data['password'])
            login(request, user)
            return redirect('/')


def auth_user(request):
    if not request.user.is_anonymous:
        return redirect('/profile/')
    if request.method == "GET":
        form = AuthorizeForm()
        return render(request, 'user/auth.html', {"form": form})
    else:
        data = {'name': request.POST.get("username"),
                'password': request.POST.get("password")}
        if not AdvUser.objects.filter(username=data['name']).exists():
            form = AuthorizeForm(request.POST)
            form.add_error('username', 'Пользователя с данным именем не существует')
            return render(request, 'user/auth.html', {'form': form, 'title': 'Авторизация'})
        else:
            user = authenticate(request, username=data['name'], password=data['password'])
            if user is not None:
                login(request, user)
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
        userBar = render_to_string('user/user_bar.html', {'isLoggedIn': isLoggedIn(request)})
        return render(request, 'user/user_details.html', {'title': 'Профиль', 'category': "Выберите категорию", 'user_bar':userBar})
    else:
        data = {'name': request.POST.get("productName")}
        products = list(Product.objects.filter(Name__contains=data['name']))
        cols = ['Название', 'Цена', 'Категория']
        rows = []
        for item in products:
            rows.append([item.Name, item.Price, item.Type.TypeName])
        return render(request, 'profile.html', {'cols': cols, 'rows': rows, 'category': f"Поиск - {data['name']}"})


# @csrf_protect
def all_books(request):
    userBar = render_to_string('user/user_bar.html', {'isLoggedIn': isLoggedIn(request)}, request=request)
    if request.method == "GET":
        return render(request, 'book_shop/main_books.html', {'categories': KnowledgeCategory.objects.all(),
                                                             'books': Book.objects.all(),
                                                             'user_content': userBar})
    if request.method == "POST":
        # поиск книг
        return render(request, 'book_shop/main_books.html', {'categories': KnowledgeCategory.objects.all(),
                                                             'books': Book.objects.filter(name__contains=request.POST.get("bookName")),
                                                             'user_content': userBar})


def all_books_by_category(request, id):
    userBar = render_to_string('user/user_bar.html', {'isLoggedIn': isLoggedIn(request)}, request=request)
    if request.method == "GET":
        return render(request, 'book_shop/main_books.html', {'categories': KnowledgeCategory.objects.all(),
                                                             'books': Book.objects.filter(category_id=id),
                                                             'user_content': userBar})
    return None


def adm_pnl(request):
    userBar = render_to_string('user/user_bar.html', {'isLoggedIn': isLoggedIn(request)}, request=request)
    return render(request, "user/admin_panel.html", {'header':["id", "category_id", "authors", "name", "publish_date", "price"],
                                                     'book_data':Book.objects.all(),
                                                     'user_content': userBar})


def delete_book(request, id):
    ob = Book.objects.get(id=id)
    if ob is not None:
        ob.delete()
    return render(request, "user/admin_panel.html", {'header':["id", "category_id", "authors", "name", "publish_date", "price"],
                                                     'book_data':Book.objects.all()})


def delete_category(request, id):
    ob = KnowledgeCategory.objects.get(id=id)
    if ob is not None:
        ob.delete()
    return render(request, "user/admin_panel.html", {'header':["id", "category_id", "authors", "name", "publish_date", "price"],
                                                     'book_data':Book.objects.all()})