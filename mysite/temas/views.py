from django.shortcuts import render
from django.views import generic

from .models import Temas
from mysite.polls.models import Perguntas

class IndexView(generic.ListView):
    template_name = 'temas/index.html'
    context_object_name = 'lista_temas'

    def get_queryset(self):
        """Retorna os temas disponíveis."""
        return Temas.objects.all()

class DetalheTemaView(generic.DetailView):
    # precisa indicar com qual model a generic view vai estar trabalhando
    model = Perguntas
    template_name = 'temas/mostra.html'
    context_object_name = 'lista_perguntas'

    def get_queryset(self, tema_id):
        """
        Excludes any questions that aren't published yet.
        """
        return Perguntas.objects.filter(pub_date__lte=timezone.now()).filter(tema.id=tema_id)

