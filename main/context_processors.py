from django.db.models import Count
from .models import Genre, Autor
import random


'''добавлено тут для отображения этих данных в боковой панели базового шаблона, в настройках надо добавить 'main.context_processors.common_context', 
в темплейтс'''

def common_context(request):
    category_genre = Genre.objects.all()
    category_genre_rand = random.sample(list(Genre.objects.all()), 2)
    autor_rand = random.sample(list(Autor.objects.all()), 2)
    
    return {
        "category_genre": category_genre,
        "category_genre_rand": category_genre_rand,
        "autor_rand": autor_rand,
    }

