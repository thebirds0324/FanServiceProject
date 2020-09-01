from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.template import loader
from datetime import datetime

def index(req):
    template=loader.get_template('index.html')
    now=datetime.now()
    print((now))
    context={
        'current_date': now,
        "value" : "바로",
    }
    return HttpResponse(template.render(context, req))
