from django.db import models

class ciudad(models.Model):
    codigo_PC = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)

    def __str__(self):
        return str(self.codigo_PC)