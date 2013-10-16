from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(
                max_length=50,
                blank=True,
                null=True)
    apellido = models.CharField(
            max_length=50,
            blank=True,
            null=True,
            )

    def __unicode__(self):
        return "%s %s" % (self.nombre, self.apellido)

class Auto(models.Model):
    duenio = models.ForeignKey(Persona)
    modelo = models.IntegerField()