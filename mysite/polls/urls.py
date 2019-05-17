from django.urls import path

from .views import *

app_name = 'perguntas'
urlpatterns = [
    path('', questoesView.as_view(), name='perguntas-index'),
    path('adiciona/', AdicionaPerguntaView.as_view(), name='perguntas-adiciona'),
    path('<pk>/', DetailView.as_view(), name='perguntas-mostra'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<pk>/edit/', edit, name='perguntas-edit'),
    path('<pk>/delete/', delete, name='perguntas-delete'),
]