from django.db import models

# Create your models here.
class servicio(models.Model):
    Codigo_S = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)
    Precio = models.IntegerField()
    Descripcion = models.TextField()

    def __str__(self):
        return str(self.Codigo_S)
