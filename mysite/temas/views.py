from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib import messages

from .forms import AdicionaTemaForm, TemaForm
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

def mostra(request, pk):
    return render(request, 'detalhe.html', {'tema': Temas.objects.get(pk=pk)})

class AdicionaTemaView(View):
    
    template_name = 'adiciona.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = AdicionaTemaForm(request.POST)
        dados_form = form.data
        novo_tema = dados_form['tema_text']

        ja_existe = Temas.objects.get(tema_text__icontains=novo_tema).exists()

        if (not ja_existe and form.is_valid()):

            Temas(tema_text=novo_tema).save()

            return redirect('/')
        
        return render(request, self.template_name, {'form' : form, 'msg_erro': "Tema já existe no sistema" })

def edit(request, pk):

    tema = get_object_or_404(Temas, pk=pk)
    form = TemaForm(request.POST or None, instance=tema)

    if request.method == 'POST':
        if form.is_valid:
            haha = form.save()            
            messages.success(request, 'Tema alterado com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Tema não alterado!')
    
    context = {
        'form': form,
        'pk': pk,
        'tema': tema
    }
    return render(request, 'edita.html', context) 

def delete(request, pk):
    tema = get_object_or_404(Temas, pk=pk)
    tema.delete()
    return redirect('/', { 'msg': "Tema deletado com sucesso" })
