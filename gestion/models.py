from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.

class Medico(models.Model):
    """
    ¦Clase 'Medico'
    """
    nombre= models.CharField(max_length=50)
    age= models.DateField()
    hospital = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Medicos"

class Farmaceutico(models.Model):
    """
    ¦Clase 'Farmaceutico'
    """
    nombre= models.CharField(max_length=50)
    age= models.DateField()
    calleDeFarmacia= models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True,on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Farmaceutico"


class Paciente(models.Model):
    """
    ¦Clase 'Paciente'
    """
    nombre= models.CharField(max_length=50)
    age= models.DateField()
    dni= models.CharField(max_length=9)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Pacientes"


class Receta(models.Model):
    """
    ¦Clase 'Receta'
    """
    medico = models.ForeignKey('Medico')
    paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)
    farmaceutico = models.ForeignKey('Farmaceutico', null=True)
    farmacos = models.CharField(max_length=100)
    duracionDias = models.IntegerField()
    unidades = models.IntegerField()
    cadaCuantasHoras = models.IntegerField()
    fecha = models.DateTimeField(default=datetime.now,blank=True)
    fechaDispensacion =  models.DateTimeField(blank=True)

    def __str__(self):
        return self.paciente.nombre+': '+self.farmacos
    class Meta:
        verbose_name_plural = "Recetas"