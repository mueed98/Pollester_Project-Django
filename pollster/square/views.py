from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse



# Get questions and display them

def index(request, num):
    context = {'latest_question_list': num * num}
    return render(request, 'square/index.html', context)