from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
from django.urls   import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('book_item/<int:my_id>/', views.book_item , name='book_item'),
    path('autor_detail/<int:my_id>/', views.autor_detail, name='autor_detail'),
    path('autor_list', views.autor_list, name='autor_list'),
    path('genre_list', views.genre_list, name='genre_list'),
    path('genre/<int:my_id>/', views.genre, name='genre')

   ]+ static(settings.MEDIA_URL,
              document_root=settings.MEDIA_ROOT)

