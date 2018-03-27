# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.db.models import Count, Sum
from .models import ProjectInfo
from django.urls import reverse
import os
import zipfile


def create_zip(path_list, save_path, project_name):
    tar_name = project_name
    for pro in path_list:
        tar_name = tar_name + '_' + pro['type']
    tar_name = tar_name + '.zip'
    new_zip = zipfile.ZipFile(save_path + tar_name, 'w')

    for pro in path_list:
        for dir_path, dir_names, file_names in os.walk(pro['path']):
            for file_name in file_names:
                file_path = os.path.join(dir_path, file_name)
                new_zip.write(file_path, project_name + '/' + pro['type'] + '/' + file_path[len(pro['path']):])

    new_zip.close()
    return tar_name


def show_list(request):
    projects = ProjectInfo.objects.values('name').annotate(count=Count('id'), size=Sum('size')).order_by('name')
    context = {'project_list': projects}
    return render(request, 'project_list.html', context)


def show_more_detail(request, project_name, type):
    items = ProjectInfo.objects.filter(name=project_name)
    types = []
    project_info = ProjectInfo()
    for item in items:
        if item.source == type:
            types.append({'name': item.source, 'active': True})
            project_info = item
        else:
            types.append({'name': item.source, 'active': False})
    context = dict()
    context['project_name'] = project_name
    context['item'] = project_info
    context['types'] = types
    if project_info.source == 'CODE':
        context['code'] = "unsupported"
    else:
        context['code'] = open(project_info.preview_path, 'r+').read(4096)
    return render(request, 'project_detail.html', context)


def show_detail(request, project_name):
    items = ProjectInfo.objects.filter(name=project_name)
    return HttpResponseRedirect(reverse('download:detail', args=(project_name, items[0].source)))


def download(request, project_name):
    types = request.POST.getlist('types')
    path_list = []
    for type in types:
        item = ProjectInfo.objects.get(name=project_name, source=type)
        path_list.append({'path': item.path, 'type': type})
    tar_name = create_zip(path_list, 'E:/', project_name)
    response = FileResponse(open('E:/' + tar_name, 'rb'), content_type="application/zip")
    response['Content-Disposition'] = 'attachment; filename="' + tar_name + '"'
    return response


def search(request):
    str = request.GET.get('str')
    projects = ProjectInfo.objects.values('name').annotate(count=Count('id'), size=Sum('size')).filter(name__contains=str).order_by('name')
    context = {'project_list': projects}
    return render(request, 'project_list.html', context)



