from enum import unique
from django.db import models

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=20)
    atentions = models.SmallIntegerField(default=0) 

class Meta_device(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    fecha_adquisicion = models.DateTimeField("fecha en que se registró")
    fecha_retiro = models.DateTimeField("fecha en que se retiró")
    area_asignado = models.CharField(max_length=20)

class Device_intern(Meta_device):
    id_label = models.CharField(max_length=7,unique=True)
    status = models.CharField(max_length=10)
    maintenance = models.SmallIntegerField(default=0)
    area_de_uso =  models.CharField(max_length=20)
    
class Device_extern(Meta_device):
    uses = models.SmallIntegerField(default=0) 

class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    numero_contacto = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    
class Schedule(models.Model):
    nombre = models.CharField(max_length=20)
    dia = models.CharField(max_length=20)
    inicio = models.CharField(max_length=20)
    fin = models.CharField(max_length=20)

class Provider(Contacto):
    Equipo = models.CharField(max_length=20)
    
class Worker(Contacto):
    Puesto = models.CharField(max_length=20)
    Horario = models.CharField(max_length=20)