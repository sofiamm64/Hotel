from django.shortcuts import render
from servicio.models import *


def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')
