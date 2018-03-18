from django.template import loader
from django.http import HttpResponse, JsonResponse
from download.syn_db import SynDB


def home(request):
    template = loader.get_template('home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def synchronize(request):
    SynDB.syn_db()
    return JsonResponse({'status': 'success'})

