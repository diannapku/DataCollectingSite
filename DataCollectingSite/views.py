from django.template import loader
from django.http import HttpResponse


def home(request):
    template = loader.get_template('home.html')
    context = {
        'info': '<p>Database synchronized!</p>',
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    context = {
        'info': '<p>Database synchronized!</p>',
    }
    return HttpResponse(template.render(context, request))

