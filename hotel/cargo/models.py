from django.db import models

# Create your models here.

class cargo(models.Model):
    Codigo_C = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=25)

    def __str__(self):
        return str(self.Codigo_C)