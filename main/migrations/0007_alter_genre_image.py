# Generated by Django 4.2.19 on 2025-02-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_genre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите обложку книги', null=True, upload_to='main/image/genre', verbose_name='Обложка'),
        ),
    ]
