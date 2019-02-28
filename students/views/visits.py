from django.shortcuts import render
from ..model.students import Student
from django.http import HttpResponse
import datetime


def visits_list(request):
    monthlocal = {'February': 'Лютий', 'Березень': 'March'}

    days_urk = {'Mon': 'Пн', 'Tue': 'Вт', 'Wed': 'Cр', 'Thu': 'Чт', 'Fri': 'Пт', 'Sat': 'Сб', 'Sun': 'Вс'}
    current_month = (datetime.date.today()).strftime('%B')
    def get_days():
        today = datetime.date.today()
        days_number = datetime.date(today.year, today.month + 1, 1) - datetime.date(today.year, today.month, 1)
        days = [i for i in range(1, int(days_number.days) + 1)]
        urk_day = [days_urk.get(i) for i in [i for i in [datetime.date(today.year, today.month, i).strftime('%a') for i in range(1, int(days_number.days))]]]
        return(days, urk_day)

    students = Student.objects.values('first_name','last_name')
    visits = students
    return render(request, 'visits.html', {'visits': visits, 'days': get_days, 'current_month': monthlocal.get(current_month), 'ukr_days':get_days})

