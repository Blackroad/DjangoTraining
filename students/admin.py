from django.contrib import admin
from .model.students import Student
from .model.group import Group
from .model.visits import Visits

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Visits)
