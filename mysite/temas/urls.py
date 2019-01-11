from django.conf.urls import include, url
from django.urls import path

from . import views

app_name = 'temas'
urlpatterns = [
    #url(r'^temas/$', include(views.index)),
    #url(r'^temas/(?P<tema_id>\d+)$', include(views.mostrar)),
    path('', views.index, name='temas-index'),
    path('adiciona/', AdicionaTemaView.as_view(), name='temas-adiciona'),
    #path('adiciona/<tema_text>/', views.salva, name='tema-salva'),
    path('<int:tema_id>/', views.mostra, name='temas-mostra'),
]