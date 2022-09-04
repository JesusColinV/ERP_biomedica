from calendar import month
import datetime
from django.db import models
from django.utils import timezone


class Day(models.Model):
    day = models.CharField(max_length=20)
    def __str__(self):
        return self.day
    
class Area(models.Model):
    name = models.CharField(max_length=20)
    atention = models.SmallIntegerField(default=0)    
    def __str__(self):
        return self.name
    

class Meta_device(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    date_adquisicion = models.DateTimeField("fecha en que se registró")
    date_retiro = models.DateTimeField("fecha en que se retiró")
    area_asignado = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
  

    
CHOISES_SCHEDULE_NAME =  (
    ("MAÑ", "MAÑANA"),
    ("TAR", "TARDE"),
    ("NOC", "NOCHE"),
    ("SPE", "ESPECIAL"),
    ("OTR", "OTRO")
)


    
class Schedule(models.Model):
    name = models.CharField(max_length=20, choices=CHOISES_SCHEDULE_NAME)
    day = models.ManyToManyField(Day)
    start = models.TimeField( auto_now=False, auto_now_add=False)
    end = models.TimeField( auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name


    
    
class Worker(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    Puesto = models.CharField(max_length=20)
    Horario = models.ForeignKey(Schedule, on_delete=models.CASCADE)  
    def __str__(self):
        return self.name
    
class Device_intern(Meta_device):
    id_label = models.CharField(max_length=7,unique=True)
    status = models.CharField(max_length=10)
    maintenance = models.SmallIntegerField(default=0)
    area_de_uso =  models.CharField(max_length=20)
    date_mantenimiento = models.DateTimeField("fecha del ultimo mantenimiento")
    
    def requires_maintenance(self):
        return self.date_mantenimiento >= timezone.now() - datetime.timedelta(month=6)

    def near_to_maintenance(self):
        return (self.date_mantenimiento >= timezone.now() - datetime.timedelta(month=5)) and (self.date_mantenimiento >= timezone.now() - datetime.timedelta(month=6))
    
    def is_old_device(self):
        return self.date_adquisicion
    
class Device_extern(Meta_device):
    uses = models.SmallIntegerField(default=0) 

class Provider(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    Equipo = models.ForeignKey(Device_extern, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
