from django.http import HttpResponse
from django.shortcuts import render

from . import models
from .models import Question


def index(request):
    question_list = models.Question.objects.order_by('create_date')
    context = {'question_list': question_list}
    return render(request, 'setdata/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'setdata/question_detail.html')
