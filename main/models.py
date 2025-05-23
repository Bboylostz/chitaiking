
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
import uuid
from django.utils import timezone
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models import F
from django.views.generic import DetailView


class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')
    



class Autor(models.Model):
    last_name = models.CharField(max_length=100, help_text='Введите фамилию автора', verbose_name='Фамилия автора')
    first_name = models.CharField(max_length=100, help_text='Введите имя автора', verbose_name='Имя автора')
    other_name = models.CharField(max_length=100, help_text='Введите отчество автора', verbose_name='Отчество автора')
    image = models.ImageField(upload_to='image/autor', blank=True, null=True,
                              help_text='Загрузите обложку книги',
                              verbose_name='Обложка')
    biography= CKEditor5Field(help_text='Введите биографию', verbose_name='Биография',blank=True, null=True,config_name='extends')


    def __str__(self):
        return self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Введите жанр', verbose_name='Жанр')
    image = models.ImageField(upload_to='image/genre', blank=True, null=True, help_text='Загрузите обложку книги',
                              verbose_name='Обложка')



    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')

    def __str__(self):
        return self.name
    


class Book(models.Model):
    tittle = models.CharField(max_length=200, help_text='Введите название', verbose_name='Название')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text='Выберите жанр', verbose_name='Жанр')
    authors = models.ManyToManyField(Autor, related_name='books', verbose_name='Авторы')
    description = models.CharField(max_length=1000, help_text='Введите описание', verbose_name='Описание')
    text = CKEditor5Field(help_text='Введите текст своего произведения', verbose_name='Текст',config_name='extends')
    image = models.ImageField(upload_to='image/book', blank=True, null=True, help_text='Загрузите обложку книги',
                              verbose_name='Обложка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.IntegerField(default=0, editable=False, verbose_name='Количество просмотров')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    def __str__(self):
        return self.tittle
    



#TODO не удаляется из папки django_ckeditor_5 необходимо доделать
# это нужно что бы удалять картинки при удалении объекта в класее, что бы они не висели в папке
# необходимо прописать код в apps.py  и добавить signals.py
@receiver(post_delete)
def delete_files(sender, instance, **kwargs):
    # Получаем все поля модели
    for field in sender._meta.get_fields():
        # Проверяем, является ли поле файловым (FileField или ImageField)
        if hasattr(field, 'storage') and hasattr(instance, field.name):
            f = getattr(instance, field.name)
            
            # Проверяем, существует ли файл и доступно ли хранилище
            if hasattr(f, 'path') and f.path:
                try:
                    # Проверяем, существует ли файл физически
                    if default_storage.exists(f.path):
                        default_storage.delete(f.path)
                    else:
                        print(f"Файл {f.path} не найден, пропускаем удаление")
                except Exception as e:
                    print(f"Ошибка при удалении файла {f.path}: {str(e)}")
                    # Логируем ошибку, но не прерываем выполнение