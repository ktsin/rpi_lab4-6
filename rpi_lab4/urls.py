"""rpi_lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import book_shop

import book_shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_shop.views.index),
    path('about/', book_shop.views.about),
    path('register/', book_shop.views.register_user),
    path('login/', book_shop.views.auth_user),
    path('books/', book_shop.views.all_books),
    path('books/<int:id>', book_shop.views.all_books_by_category),
    path('adminpanel/', book_shop.views.adm_pnl),

    # books CRUD
    path('books/delete/<int:id>', book_shop.views.delete_book),
    path('books/edit/<int:id>', book_shop.views.delete_book),
    path('books/add/', book_shop.views.delete_book),
    # end books

    # users CRUD
    path('users/delete/<int:id>', book_shop.views.delete_book),
    path('users/edit/<int:id>', book_shop.views.delete_book),
    path('users/add/', book_shop.views.delete_book),
    # end users

    # authors CRUD
    path('authors/delete/<int:id>', book_shop.views.delete_book),
    path('authors/edit/<int:id>', book_shop.views.delete_book),
    path('authors/add/', book_shop.views.delete_book),
    # end authors

    # income CRUD
    path('income/delete/<int:id>', book_shop.views.delete_book),
    path('income/edit/<int:id>', book_shop.views.delete_book),
    path('income/add/', book_shop.views.delete_book),
    # end income

    # outcome CRUD
    path('outcome/delete/<int:id>', book_shop.views.delete_book),
    path('outcome/edit/<int:id>', book_shop.views.delete_book),
    path('outcome/add/', book_shop.views.delete_book),
    # end outcome
]
