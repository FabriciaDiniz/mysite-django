from django.shortcuts import render
from django.views import generic

from .models import Temas

class IndexView(generic.ListView):
    template_name = 'temas/index.html'
    context_object_name = 'lista_temas'

    def get_queryset(self):
        """Retorna os temas disponíveis."""
        return Temas.objects.all()
