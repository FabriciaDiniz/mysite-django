from django.shortcuts import render

from .models import Temas
from mysite.polls.models import Perguntas

#TODO: tirar esses negócios e fazer só as funções bonitinhas
def index(request):
    return render(request, 'index.html')

#def mostrar(request, tema_id):
#    perguntas = Temas.objects.get(id=tema_id)
#    return render(request, 'perfil.html', {"lista_perguntas" : perguntas})