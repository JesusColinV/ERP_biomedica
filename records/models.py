from pydoc import describe
from django.db import models

# Create your models here.
class Orden(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    description = models.CharField(max_length=100) 
    area = models.CharField(max_length=20)
    equipo = models.CharField(max_length=20)
    evaluacion = models.CharField(max_length=20)
    initial_state = models.CharField(max_length=20)
    final_state = models.CharField(max_length=20)
    
class Reporte(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    reporta = models.CharField(max_length=20)
    atiende = models.CharField(max_length=20)
    reponsable = models.CharField(max_length=20)
    
class Salidas(models.Model):
    equipo = models.CharField(max_length=20) 
    provedor = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()