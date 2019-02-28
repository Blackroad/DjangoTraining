from django.db import models
import itertools
import datetime

days_urk = {'Mon': 'Пн', 'Tue': 'Вт', 'Wed': 'Cр', 'Thu': 'Чт', 'Fri': 'Пт', 'Sat': 'Сб', 'Sun': 'Вс'}

def get_days():
    today = datetime.date.today()
    days_number = datetime.date(today.year, today.month + 1, 1) - datetime.date(today.year, today.month, 1)
    days = [i for i in range(1, int(days_number.days) + 1)]
    ukr_day = [days_urk.get(i) for i in [i for i in [datetime.date(today.year, today.month, i).strftime('%a') for i in range(1, int(days_number.days)+1)]]]
    f = list(map(list, zip(ukr_day,days)))
    for i in f:
        print(i[0] + str(i[1]))





get_days()

