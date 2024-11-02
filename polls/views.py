from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
# from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_five = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = { 'latest_question_list': latest_five }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     qq = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    qq = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': qq})

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, ChoiceDoesNotExist):
        # redisplay question voting form with error
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': 'you didnt select a choice bozo'
            }
        )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))