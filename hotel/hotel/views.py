from django.shortcuts import render
from servicio.models import *


def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def habitacion(request):
    return render(request, 'habitacion.html')

def paquetes(request):
    objpaquete = paquetes.objects.all()

    contex = {
        'paq': objpaquete,
    }
    return render(request, 'paquetes.html', contex)


def servicios(request):
    objservicios = servicio.objects.all()

    context = {
        'serv': objservicios,
    }
    return render(request, 'servicios.html', context)