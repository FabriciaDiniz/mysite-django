from django.shortcuts import render

from .models import Temas
from mysite.polls.models import Perguntas

def index(request):
    lista_temas = Temas.objects.all()
    context = {
        'lista_temas' : lista_temas
    }
    return render(request, 'index.html', context)

def adiciona(request):
    return render(request, 'adiciona.html')

def mostra(request, tema_id):
    perguntas = Perguntas.objects.get(id=tema_id)
    return render(request, 'detalhe.html', {"lista_perguntas" : perguntas})