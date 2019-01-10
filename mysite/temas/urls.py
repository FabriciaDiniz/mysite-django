from django.conf.urls import include, url
from django.urls import path

from . import views

app_name = 'temas'
urlpatterns = [
    #url(r'^temas/$', include(views.index)),
    #url(r'^temas/(?P<tema_id>\d+)$', include(views.mostrar)),
    path('', views.index, name='index'),
    path('adiciona/', views.adiciona, name='adiciona'),
    #path('<int:tema_id>/', views.mostra, name='mostra'),
]