# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
    return render(request, 'students/students_list.html', {})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups_list(request):
    return render(request, 'students/groups_list.html', {})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
# Create your views here.
def students_list(request):
    students = (
    {'id': 1,
    'first_name': u'Віталій',
    'last_name': u'Костирка',
    'ticket': 235,
    'image': 'img/bv1.jpg'},
    {'id': 2,
    'first_name': u'Дудаp',
    'last_name': u'Юрій',
    'ticket': 2123,
    'image': 'img/bv2.jpg'},
    {'id': 3,
     'first_name': u'Маркелло',
     'last_name': u'Натанаїл',
     'ticket': 2124,
     'image': 'img/SetterVet.jpg'}
    )
    return render(request, 'students/students_list.html',{'students': students})

def visiting(request):
    return render(request, 'students/visiting.html', {})
# def visiting(request):
#     month=()
#     for i in range(31):
#         month[i]=i+1
#     return render(request, 'students/visiting.html', {'month': month})