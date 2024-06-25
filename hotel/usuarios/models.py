from django.db import models

class Usuarios(models.Model):
    Elegir_Rol = [
        (1, 'Empleado'),
        (2, 'Administrador'),
    ]
    
    Documento = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    Correo = models.CharField(max_length=15, unique=True)
    Celular = models.CharField(max_length=15, unique=True)
    Rol = models.IntegerField(choices=Elegir_Rol, default=1, null=True, blank=True)
