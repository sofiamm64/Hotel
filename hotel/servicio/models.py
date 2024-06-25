from django.db import models

# Create your models here.
class servicio(models.Model):
    Codigo_S = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)
    Precio = models.IntegerField()
    Descripcion = models.TextField()

    def __str__(self):
        return str(self.Codigo_S)
    
class habitacion(models.Model):
    Codigo_H = models.CharField(max_length=20, primary_key=True)
    Tipo = models.CharField(max_length=1)
    Precio = models.FloatField()
    Estado = models.CharField(max_length=20)
    Posicion = models.TextField() 
    Piso = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Codigo_H)

class paquetes(models.Model):
    Codigo_Pa = models.CharField(max_length=20, primary_key=True)
    Ciudad = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=25)
    Precio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.Codigo_Pa