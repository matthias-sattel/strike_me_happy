from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Pin

def index(request):
    output = Pin.objects.order_by('-creation_date').filter(done=False)
    template = loader.get_template('pins/index.html')
    context = RequestContext(request, {
        'open_pins_list': output,
        })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse(Pin.objects.filter(id=question_id))
