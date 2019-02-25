from django.contrib import admin
from .model.students import Student
from .model.group import Group

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
