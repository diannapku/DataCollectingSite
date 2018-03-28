from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'upload_home.html')


def handle_uploaded_file(f):
    with open('E:/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        f = request.FILES['myfile']
        handle_uploaded_file(f)
        return HttpResponse("success")

    return HttpResponse("fail")
