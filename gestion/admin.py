from django.contrib import admin
from gestion.models import *

# Register your models here.

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Farmaceutico)
admin.site.register(Receta)