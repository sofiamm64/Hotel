
from django.db import models

class Cliente(models.Model):
    Documento_C = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    celular = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)
    genero = models.CharField(max_length=1)
    f_Nacimiento = models.DateTimeField()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
