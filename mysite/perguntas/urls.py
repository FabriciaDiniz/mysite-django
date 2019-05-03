from django.urls import path

from .views import *

app_name = 'perguntas'
urlpatterns = [
    path('', questoesView.as_view(), name='perguntas-index'),
    path('perguntas/adiciona/', AdicionaPerguntaView.as_view(), name='perguntas-adiciona'),
    path('perguntas/<pk>/', DetailView.as_view(), name='perguntas-mostra'),
    path('perguntas/<pk>/edit/', edit, name='perguntas-edit'),
    path('perguntas/<pk>/delete/', delete, name='perguntas-delete'),
]