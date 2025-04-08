
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from django.contrib.auth import logout
from django.shortcuts import redirect


import random
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, LoginForm

def book_item(request, my_id):
    book=get_object_or_404(Book, id=my_id)
    paginator = Paginator(book.text.split('.'), 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request, 'main/book_item.html',{'book':book,
                                                  'page_obj': page_obj})


def autor_list(request,):
    autor=Autor.objects.all().order_by('last_name')
    return render(request, 'main/autor_list.html',{'autor':autor})

def autor_detail(request, my_id):
    autor=get_object_or_404(Autor, pk=my_id)
    author = Autor.objects.get(id=my_id)  # получаем автора
    books = Book.objects.all().filter(authors=my_id)
    return render(request, 'main/autor_detail.html',{'autor':autor,
                                                     'books':books,})
    

def genre_list(request):
    genre = Genre.objects.all().order_by('name')
    return render(request, 'main/genre_list.html', {'genre':genre})

def genre(request, my_id):
    genre = get_object_or_404(Genre, id=my_id)
    books = Book.objects.select_related('genre').filter(genre_id=my_id)

    return render(request, 'main/genre.html', {'genre':genre,
                                               'books':books})

def book_list(request):
    book = Book.objects.all().order_by('tittle')
    return render(request, 'main/book_list.html', {'book': book})




def index(request):
    book=random.sample(list(Book.objects.all()),3)
    genre=Genre.objects.all()
    autor=Autor.objects.all()
    return render(request, 'main/index.html', {'book': book,
                                               'genre':genre,
                                               'autor':autor})
def tag_list(request, my_id):
    selected_tag = get_object_or_404(Tag, pk=my_id)
    books = Book.objects.filter(tags=selected_tag)
    
    context = {
        'books': books,
        'selected_tag': selected_tag
    }
    return render(request, 'main/tag_list.html', context)



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()          # Сохраняем нового пользователя
            login(request, user)        # Выполняем вход
            return redirect('home')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(request, user)     # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')