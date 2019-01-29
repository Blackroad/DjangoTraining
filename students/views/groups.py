from django.shortcuts import render
from django.http import HttpResponse


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
