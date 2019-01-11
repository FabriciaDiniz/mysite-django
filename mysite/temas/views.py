from django.shortcuts import render, redirect
from django.views.generic.base import View
from forms import AdicionaTemaForm

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

# def salva(request, tema_text):
#     #inserir mensagem de sucesso se tiver dado certo
#     Temas(tema_text=tema_text).save()
#     return redirect('index')

def mostra(request, tema_id):
    return render(request, 'detalhe.html', {'tema' : Temas.objects.get(pk=tema_id)})

class AdicionaTemaView(View):
    
    template_name = 'adiciona.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = AdicionaTemaForm(request.POST)

        if form.is_valid():
            dados_form = form.data

            Temas(tema_text=dados_form['tema_text']).save()

            return redirect('index')
        
        return render(request, self.template_name, {'form' : form })