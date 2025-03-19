from django.contrib import admin
from .models import Book,Genre,Autor,Tag
# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Autor)
admin.site.register(Tag)
