@REM from django.db import models

@REM class empresa(models.Model):
@REM     Nit = models.CharField(max_length=20, primary_key=True)
@REM     nombre = models.CharField(max_length=25)
@REM     slogan = models.CharField(max_length=30)
@REM     correo = models.EmailField(max_length=30)
@REM     celular = models.CharField(max_length=15)
@REM     descripcion = models.TextField()
@REM     codigo_PC =  models.ForeignKey(codigo_PC, max_length=20,on_delete=models.SET_NULL,null=True,blank=True, db_column='codigo_PC')

@REM     def __str__(self):
@REM         return str(self.Nit)