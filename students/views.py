from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Views for Students
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


# Views for Groups
def groups_list(request):
    groups = (
        {'group_id': 1,
         'group_name': u'МтМ-21',
         'leader': u'Ячменев Олег'
         },
        {'group_id': 2,
         'group_name': u'МтМ-22',
         'leader': u'Віталій Подоба'
         },
        {'group_id': 3,
         'group_name': u'МтМ-23',
         'leader': u'Іванов Андрій'
         },
    )
    return render(request, 'group.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Add Form %s</h1>' %gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


# Views for visits
def visits_list(request):
    return HttpResponse('<h1>Attentions Listing</h1>')
