from django.conf.urls import include, url
from django.urls import path

from .views import *

app_name = 'temas'
urlpatterns = [
    #url(r'^temas/$', include(views.index)),
    #url(r'^temas/(?P<tema_id>\d+)$', include(views.mostrar)),
    path('', index, name='temas-index'),
    path('adiciona/', AdicionaTemaView.as_view(), name='temas-adiciona'),
    path('<int:pk>/', mostra, name='temas-mostra'),
    path('<int:pk>/edit/', edit, name='temas-edit'),
    path('<int:pk>/delete/', delete, name='temas-delete'),
]