from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    return HttpResponse('this is main page')


def hello_world(request):
    return HttpResponse('hello world page')