from django.db import models
from cargo.models import cargo

class usuario(models.Model):
    Elegir_Rol = [
        (1, 'Empleado'),
        (2, 'Administrador'),
    ]
    
    Documento = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    Correo = models.CharField(max_length=15, unique=True)
    Celular = models.CharField(max_length=15, unique=True)
    cargo =  models.ForeignKey(cargo, on_delete=models.CASCADE, db_column='Codigo_C')

    def __str__(self):
            return str(self.Documento)