from importlib.resources import contents
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse


import random
from .models import *


def book_item(request, my_id):
    book=get_object_or_404(Book, id=my_id)
    

    return render(request, 'main/book_item.html',{'book':book})


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




def index(request):
    book=random.sample(list(Book.objects.all()),3)
    genre=Genre.objects.all()
    autor=Autor.objects.all()
    return render(request, 'main/index.html', {'book': book,
                                               'genre':genre,
                                               'autor':autor})



