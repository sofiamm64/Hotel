from django.shortcuts import render
from .models import servicio
from .models import paquetes

def ad_servicios(request):
    servicios = servicios.objects.all()
    return render(request, 'servicios.html',{'servicios': servicios})

def ad_paquetes(request):
    pacq = paquetes.objects.all()
    return render(request, 'paquetes.html',{'pacq': pacq})


def ad_habitacion(request):
    servs = habitacion.objects.all()
    return render(request, 'habitacion.html',{'servs': servs})