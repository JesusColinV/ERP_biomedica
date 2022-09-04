from django.contrib import admin
from .models import *

admin.site.register(Area)
admin.site.register(Day)
admin.site.register(Schedule)
admin.site.register(Provider)
admin.site.register(Worker)
admin.site.register(Device_intern)
admin.site.register(Device_extern)