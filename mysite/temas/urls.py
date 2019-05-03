from django.conf.urls import include, url
from django.urls import path

from .views import *

app_name = 'temas'
urlpatterns = [
    path('', index, name='temas-index'),
    path('temas/adiciona/', AdicionaTemaView.as_view(), name='temas-adiciona'),
    path('temas/<pk>/', mostra, name='temas-mostra'),
    path('temas/<pk>/edit/', edit, name='temas-edit'),
    path('temas/<pk>/delete/', delete, name='temas-delete'),
]