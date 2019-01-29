from django.shortcuts import render
from django.http import HttpResponse


def visits_list(request):
    return HttpResponse('<h1>Attentions Listing</h1>')
