from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import PerguntaForm, AdicionaPerguntaForm

from mysite.polls.models import Perguntas
from mysite.temas.models import Temas
from mysite.opcoes.models import Opcoes

class questoesView(generic.ListView):
    model = Perguntas
    template_name = 'perguntas/index.html'
    context = 'ultimas_perguntas_lista'

    def get_queryset(self):
        """Return the last published questions (not including those set to be
        published in the future)."""
        return Perguntas.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')


class AdicionaPerguntaView(View):
    template_name = 'perguntas/adiciona.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = AdicionaPerguntaForm(request.POST)
        dados_form = form.data
        nova_pergunta = dados_form['pergunta_text']

        ja_existe = Perguntas.objects.get(pergunta_text__icontains=nova_pergunta).exists()

        if not ja_existe and form.is_valid():
            Perguntas(pergunta_text=nova_pergunta).save()

            return redirect('/')

        return render(request, self.template_name, {'form': form, 'msg_erro': "Pergunta já existe no sistema"})

class DetailView(generic.DetailView):
    # precisa indicar com qual model a generic view vai estar trabalhando
    model = Perguntas
    template_name = 'perguntas/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Perguntas.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Perguntas
    template_name = 'perguntas/results.html'

def vote(request, question_id):
    pergunta = get_object_or_404(Perguntas, pk=question_id)
    try:
        selected_choice = pergunta.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Opcoes.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'perguntas/detail.html', {
            'pergunta': pergunta,
            'error_message': "Você não escolheu uma opção.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('perguntas:results', args=(pergunta.id,)))

def results(request, question_id):
    pergunta = get_object_or_404(Perguntas, pk=question_id)
    return render(request, 'perguntas/results.html', {'pergunta': pergunta})


def edit(request, pk):
    pergunta = get_object_or_404(Perguntas, pk=pk)
    form = PerguntaForm(request.POST or None, instance=pergunta)

    if request.method == 'POST':
        if form.is_valid:
            haha = form.save()
            messages.success(request, 'Pergunta alterada com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Pergunta não alterada!')

    context = {
        'form': form,
        'pk': pk,
        'tema': tema
    }
    return render(request, 'edita.html', context)


def delete(request, pk):
    pergunta = get_object_or_404(Perguntas, pk=pk)
    pergunta.delete().save()
    return redirect('/', {'msg': "Pergunta deletada com sucesso"})

