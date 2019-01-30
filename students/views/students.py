from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name':u'Віталій',
         'last_name':u'Подоба',
         'ticket': 235,
         'image':'img/podoba3.jpg'},
        {
          'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123 ,
         'image': 'img/me.jpeg'},
        {'id': 3,
         'first_name': u'Притула',
         'last_name': u'Тарас',
         'ticket': 3312,
         'image': 'img/piv.png'},
    )
    return render(request, 'students_list.html', {'students':students})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)