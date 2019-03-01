from django.shortcuts import render
from students.model.students import Student
# from django.http import HttpResponse
from ..static.localization_data.date_translation import DateTranslation
import datetime


def get_days():
    # get date from local machine
    today = datetime.date.today()
    # calculate number of days in current month and create a list for it
    days_number = datetime.date(today.year, today.month + 1, 1) - datetime.date(today.year, today.month, 1)
    days = [i for i in range(1, int(days_number.days) + 1)]
    # create list of named weekdays for each day using ukr translation from imported DateTranslation class
    ukr_day = [DateTranslation.days_urk.get(i) for i in [i for i in [datetime.date(today.year, today.month, i).strftime('%a') for i in range(1, int(days_number.days) + 1)]]]
    # compiling number of days in month with weekdays names to receive list like [[Пн,1],[Вт,2]...]
    compile_days = list(map(list, zip(ukr_day, days)))
    # packing all in list with format ['Пн,1' , 'Вт,2,', ....] and return it
    list_default = []
    for i in compile_days:
        list_default.append(('{} {}'.format(i[0], i[1])))
    compile_days = list_default
    return compile_days


def visits_list(request):
    # Get translated  month from localization class
    all_month = DateTranslation.month_local
    # Get current month in from system date
    current_month = (datetime.date.today()).strftime('%B')
    # get compile weekdays with number days
    compile_days = get_days()
    visits = Student.objects.values('first_name', 'last_name').order_by('last_name')
    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'last_name'):
        visits = visits.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            visits = visits.reverse()
    return render(request, 'visits.html', {'visits': visits, 'days': compile_days, 'current_month': all_month.get(current_month)})
