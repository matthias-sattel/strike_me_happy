from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from datetime import datetime
from .models import Pin
from .forms import PinForm


def index(request):
    #logger.debug('pins')
    if request.method == 'POST':
        form = PinForm(request.POST)
        if form.is_valid():
            #logger.debug('new pin')
            title=form.cleaned_data['title']
            pin = Pin()
            pin.title=title
            pin.done=False
            pin.creation_date = datetime.utcnow()
            pin.save()

    else:
        form = PinForm()
    
    template = loader.get_template('index.html')
    output = Pin.objects.order_by('-creation_date').filter(done=False)
    #context = RequestContext(request, {
    #    'open_pins_list': output,
    #    })
    #return HttpResponse(template.render(context))
    return render(request, 'index.html', {'open_pins_list': output, 'form': form})

def detail(request, pin_id):
    try:
        pin = Pin.objects.get(id=pin_id)
    except Pin.DoesNotExist:
        raise Http404("Pin does not exist")
    return render(request, 'detail.html', {
        'pin': pin,
        })

def done(request, pin_id):
    pin = Pin.objects.get(id=pin_id)
    pin.done=True
    pin.save()
    return redirect('index')
