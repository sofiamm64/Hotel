from django.db import models
from ciudad.models import ciudad

class empresa(models.Model):
    Nit = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=25)
    slogan = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)
    descripcion = models.TextField()
    codigo_PC =  models.ForeignKey(ciudad, on_delete=models.CASCADE, db_column='codigo_PC')

    def __str__(self):
       return str(self.Nit)