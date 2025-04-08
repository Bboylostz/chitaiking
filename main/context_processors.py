from django.db.models import Count
from .models import Book, Genre, Autor
import random


'''добавлено тут для отображения этих данных в боковой панели базового шаблона, в настройках надо добавить 'main.context_processors.common_context', 
в темплейтс'''

def common_context(request):
    category_genre = Genre.objects.all()
    category_genre_rand = random.sample(list(Genre.objects.all()), 2)
    autor_rand = random.sample(list(Autor.objects.all()), 2)
    category_book =random.sample( list(Book.objects.all()), 3)
    
    return {
        "category_genre": category_genre,
        "category_genre_rand": category_genre_rand,
        "autor_rand": autor_rand,
        "category_book":category_book,
    }
'''для отображения пользователя'''
def auth_context(request):
    return {
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None,
    }