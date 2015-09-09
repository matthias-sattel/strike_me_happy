from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Pin

def index(request):
    output = Pin.objects.order_by('-creation_date').filter(done=False)
    template = loader.get_template('pins/index.html')
    context = RequestContext(request, {
        'open_pins_list': output,
        })
    return HttpResponse(template.render(context))

def detail(request, pin_id):
    try:
        pin = Pin.objects.get(id=pin_id)
    except Pin.DoesNotExist:
        raise Http404("Pin does not exist")
    return render(request, 'pins/detail.html', {
        'pin': pin,
        })
