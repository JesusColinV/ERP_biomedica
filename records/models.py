from time import timezone
from django.db import models
from objects.models import Area, Device_extern, Device_intern, Worker, Provider

# Create your models here.

class Evaluations(models.Model):
    description = models.CharField(max_length=150)


    
class Reporte(models.Model):
    date = models.DateField()
    time = models.TimeField()
    reporta = models.ForeignKey(Area, on_delete=models.CASCADE)
    atiende = models.CharField(max_length=100) 
    reponsable = models.ForeignKey(Worker, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
class Orden(models.Model):
    report = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=100) 
    equipo = models.ForeignKey(Device_intern, on_delete=models.CASCADE)
    evaluacion = models.CharField(max_length=100) 
    initial_state = models.CharField(max_length=100) 
    final_state = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.id
    
class Salida(models.Model):
    equipo = models.ForeignKey(Device_extern, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.equipo

class Salida_interno(models.Model):
    equipo = models.ForeignKey(Device_intern, on_delete=models.CASCADE) 
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.equipo
    