from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
# Create your views here.

def students_list(request, sid):
    try:
        sid = int(sid)
    except ValueError:
        raise Http404
    return render(request, 'demo.html', {})
