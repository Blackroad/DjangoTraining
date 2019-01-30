from django.db import models
import datetime
# Create your models here.


def date(year,month):
    date = datetime.date(year,month+1,1) - datetime.date(year,month,1)
    days = date.days
    print(days)





date(2018,10)