from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import AdicionaTemaForm
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
        dados_form = form.data
        novo_tema = dados_form['tema_text']

        ja_existe = Temas.objects.filter(tema_text__icontains=novo_tema).exists()

        if (not ja_existe and form.is_valid()):

            Temas(tema_text=novo_tema).save()

            return redirect('/temas/')
        
        return render(request, self.template_name, {'form' : form, 'msg_erro' : "Tema já existe no sistema" })