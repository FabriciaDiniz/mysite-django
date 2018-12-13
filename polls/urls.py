from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<theme>/', views.show_questions, name='theme')
    path('<theme>/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<theme>/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<theme>/<int:question_id>/vote/', views.vote, name='vote'),
]