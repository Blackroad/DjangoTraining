from django.shortcuts import render
from django.http import HttpResponse


def visits_list(request):
    visits = (
        {'id': 1,
         'student': u'Подоба Віталій'
         },
        {
         'id': 2,
         'student': u'Корост Андрій'
        },
        {'id': 3,
         'student': u'Притула Тарас'
         },
    )

    return render(request, 'visits.html', {'visits': visits})
