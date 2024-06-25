from django.db import models
from servicio.models import *
from usuarios.models import usuario
from empresa.models import empresa
from factura.models import *
from ciudad.models import ciudad
from cliente.models import cliente




class reserva(models.Model):
    codigo_R = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    fecha_de_entrada = models.DateTimeField()
    estado = models.CharField(max_length=20)
    fecha_de_salida = models.DateTimeField()
    codigo_PC =  models.ForeignKey(ciudad, on_delete=models.CASCADE, db_column='codigo_PC')
    Nit = models.ForeignKey(empresa, on_delete=models.CASCADE, db_column='Nit')
    Documento_C = models.ForeignKey(cliente, on_delete=models.CASCADE, db_column='Documento_C')
    Documento = models.ForeignKey(usuario, on_delete=models.CASCADE, db_column='Documento')
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.codigo_R)



# Create your models here.
class dtllservicio(models.Model):
    Codigo_DS = models.CharField(max_length=20, primary_key=True)
    Codigo_S = models.ForeignKey(servicio, on_delete=models.CASCADE, db_column='odigo_S')
    Codigo_R = models.ForeignKey('reserva', on_delete=models.CASCADE, db_column='Codigo_R')
    Cantidad = models.SmallIntegerField()
    Precio = models.IntegerField()

    def __str__(self):
        return str(self.Codigo_DS)


class dtllhabitacion(models.Model):
    Codigo_DH = models.CharField(max_length=20, primary_key=True)
    Cantidad = models.SmallIntegerField()
    Precio = models.FloatField()
    Codigo_R = models.ForeignKey(reserva, on_delete=models.CASCADE, db_column='Codigo_R')
    Codigo_H = models.ForeignKey(habitacion, on_delete=models.CASCADE, db_column='Codigo_H')

    def __str__(self):
        return str(self.Codigo_DH)


class dtllpaquete(models.Model):
    Codigo_DPA = models.CharField(max_length=20, primary_key=True)
    Cantidad = models.SmallIntegerField()
    Precio = models.FloatField()
    Codigo_Pa = models.ForeignKey(paquetes, null=True, on_delete=models.SET_NULL, db_column='Codigo_Pa')
    Codigo_R = models.ForeignKey(reserva, on_delete=models.CASCADE, db_column='Codigo_R')

    def __str__(self):
        return str(self.Codigo_DPA)