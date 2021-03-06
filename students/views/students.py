from django.shortcuts import render
from ..model.students import Student
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def students_list(request):
    students = Student.objects.order_by('last_name')
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    # paginate students
    paginator = Paginator(students, 5)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g 99999), deliver
        # Lst page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'students_list.html', {'students': students})


def students_add():
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
