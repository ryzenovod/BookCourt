from django.shortcuts import render
from .models import book


def index(request):
    books = book.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'books': books})


def about(request):
    return render(request, 'main/about.html')
