from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def productos(request):
    return render(request,'produc.html')

def servicio(request):
    return render(request,'servic.html')

def contacto(request):
    return render(request,'contac.html')