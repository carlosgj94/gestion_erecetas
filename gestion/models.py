from django.db import models

# Create your models here.
#receta
#medico
#farmaceutico
#paciente


class Medico(models.Model):
    """
    ¦Clase 'Medico'
    """
    nombre= models.CharField(max_length=50)
    age= models.DateField()
    hospital = models.CharField()
    especialidad = models.CharField()

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
    farmacos = models.CharField()
    duracionDias = models.IntegerField()
    unidades = models.IntegerField()
    cadaCuantasHoras = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Cities"