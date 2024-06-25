from django.shortcuts import render
from .models import servicio
from .models import paquetes

def ad_servicios(request):
    servicios = servicio.objects.all()
    return render(request, 'servicios.html',{'servicios': servicios})

def ad_paquetes(request):
    return render(request, 'paquetes.html')
