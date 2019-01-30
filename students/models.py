from django.db import models
import datetime
# Create your models here.


def date(year,month):
    date = datetime.date(year,month+1,1) - datetime.date(year,month,1)
    days = date.days
    i = [i for i in range(1,days+1)]
    for item in i:
        print (item)




date(2018,10)