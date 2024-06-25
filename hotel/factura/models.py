from django.db import models
from reservar.models import reserva



class Forma_P(models.Model):
    Codigo_FP = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)

    def __str__(self):
        return str(self.codigo_FP)
        
class factura(models.Model):
    Codigo_f = models.AutoField(primary_key=True)
    Fecha = models.DateTimeField()
    Subtotal = models.FloatField()
    iva = models.FloatField()
    Total = models.FloatField()
    codigo_R = models.ForeignKey(reserva, on_delete=models.CASCADE, db_column='codigo_R')
    codigo_FP = models.ForeignKey(Forma_P, on_delete=models.CASCADE, db_column='Codigo_FP')

    def __str__(self):
        return str(self.Codigo_f)
