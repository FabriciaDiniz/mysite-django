from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from mysite.models import Choice, Question, Theme

#class IndexView(generic.ListView):
#    template_name = 'polls/index.html'
#    context_object_name = 'latest_question_list'
#
#    def get_queryset(self):
#        """Return the last five published questions (not including those set to be
#        published in the future)."""
#        return Question.objects.filter(
#            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'theme_list'

    def get_queryset(self):
        """Return the themes available."""
        return Theme.objects.all()

class ThemeView(generic.ListView):
    model = Question
    template_name = 'polls/theme.html'
    context_object_name = 'latest_question_list'

def show_questions(request, theme_text):
    theme = get_object_or_404(Theme, pk=theme_text)
    return render(request, 'polls/theme.html', {
        'latest_question_list': Question.objects.filter(theme=theme_text)})

class DetailView(generic.DetailView):
    # precisa indicar com qual model a generic view vai estar trabalhando
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})