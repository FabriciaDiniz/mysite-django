from django.urls import path

from . import views

app_name = 'temas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    url(r'^(?P<tema_id>\d+)$', views.DetalheTemaView.as_view()),
]