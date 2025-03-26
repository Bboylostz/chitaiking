from django.contrib import admin
from .models import Article, Book,Genre,Autor,Tag
# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Autor)
admin.site.register(Tag)
admin.site.register(Article)
