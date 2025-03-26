from importlib.resources import contents
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q


import random
from .models import *


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

