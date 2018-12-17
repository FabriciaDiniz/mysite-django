from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from mysite.polls.models import Perguntas
from mysite.temas.models import Temas
from mysite.opcoes.models import Opcoes

class questoesView(generic.ListView):
    model = Perguntas
    template_name = 'polls/index.html'
    context_object_name = 'ultimas_perguntas_lista'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be
        published in the future)."""
        return Perguntas.objects.filter(tema = self.).filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     # precisa indicar com qual model a generic view vai estar trabalhando
#     model = Perguntas
#     template_name = 'polls/detail.html'
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Perguntas.objects.filter(pub_date__lte=timezone.now())

# class ResultsView(generic.DetailView):
#     model = Perguntas
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     pergunta = get_object_or_404(Perguntas, pk=question_id)
#     try:
#         selected_choice = pergunta.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Opcoes.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'pergunta': pergunta,
#             'error_message': "Você não escolheu uma opção.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(pergunta.id,)))

# def results(request, question_id):
#     pergunta = get_object_or_404(Perguntas, pk=question_id)
#     return render(request, 'polls/results.html', {'pergunta': pergunta})