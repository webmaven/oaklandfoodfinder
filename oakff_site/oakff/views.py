from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext, loader
from oakff.models import *

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {
        'message': 'Hello World!',
    })
    return HttpResponse(t.render(c))
