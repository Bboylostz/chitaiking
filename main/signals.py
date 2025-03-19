from django.db.models.signals import post_delete
from .models import Book, Autor, Genre
from django.dispatch import receiver

@receiver(post_delete, sender=Book)
def book_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_delete, sender=Autor)
def autor_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_delete, sender=Genre)
def genre_delete(sender, instance, **kwargs):
    instance.image.delete(False)