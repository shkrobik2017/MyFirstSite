from django.shortcuts import render
from .models import *

def index(request):
    posts = Product.objects.all()
    cats = Category.objects.all()
    return render(request, 'shopmain/home.html', {'cats': cats, 'posts': posts, 'title': 'Home'})

def cat_burger(request):
    posts = Product.objects.all()
    return render(request, 'shopmain/burgers.html', {'posts': posts, 'title': 'Бургеры'})

def cat_panini(request):
    posts = Product.objects.all()
    return render(request, 'shopmain/panini.html', {'posts': posts, 'title': 'Паніні'})

def cat_salad(request):
    posts = Product.objects.all()
    return render(request, 'shopmain/salad.html', {'posts': posts, 'title': 'Салати'})

def cat_bageta(request):
    posts = Product.objects.all()
    return render(request, 'shopmain/bageta.html', {'posts': posts, 'title': 'Багети'})
