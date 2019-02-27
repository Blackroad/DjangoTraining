from django.shortcuts import render
from ..model.group import Group
from django.http import HttpResponse
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def groups_list(request):
    groups = Group.objects.order_by('title')
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    return render(request, 'group.html', {'groups': groups})


def groups_add():
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(gid):
    return HttpResponse('<h1>Edit Add Form %s</h1>' % gid)


def groups_delete(gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
