# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404

from .models import Question
from django.template import loader


def index(request):
	'''shortcut render return render(request,'polls/index.html',context)'''
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
		'latest_question_list':latest_question_list,
		}
	return HttpResponse(template.render(context,request))

def detail(request,question_id):
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question':question})
def results(request,question_id):
	response="You're looking the results of question %s."
	return HttpResponse(response % question_id)
def vote(request,question_id):
	return HttpResponse("you're voting on question %s."% question_id)
