# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Student
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def students_list(request):
    students = Student.objects.all().order_by("last_name")
    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket','id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver
    # last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'students/students_list.html',{'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups_list(request):
    groups=(
    {
      'id':1,
      'name':u'ПМ-21',
      'starosta':u'Глуховецький Тарас'
    },
    {
        'id':2,
        'name':u'ПМ-22',
        'starosta':u'Корост Михайло'
    },
    {
        'id': 3,
        'name': u'МП-22',
        'starosta': u'Марків Олег'
    }
    )
    return render(request, 'students/groups_list.html', {'groups':groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


# Create your views here.


def visiting(request):
    return render(request, 'students/visiting.html', {})

