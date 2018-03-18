# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Count
from .models import ProjectInfo


def show_list(request):
    projects = ProjectInfo.objects.values('name').annotate(count=Count('id')).order_by('name')
    context = {'project_list': projects}
    return render(request, 'project_list.html', context)


def show_detail(request, project_name):
    print(project_name)
    return HttpResponse('hello world')
