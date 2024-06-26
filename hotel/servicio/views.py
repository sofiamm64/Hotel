from django.shortcuts import render
from .models import servicio
from .models import paquetes
from .models import habitacion

def ad_servicios(request):
    servicios = servicio.objects.all()
    return render(request, 'servicios.html',{'servicios': servicios})

def ad_habitacion(request):
    habitaciones = habitacion.objects.all()
    return render(request, 'habitacion.html',{'habitaciones': habitaciones})

def ad_paquetes(request):
    paquete = paquetes.objects.all()
    return render(request, 'paquetes.html',{'paquetes': paquete})


