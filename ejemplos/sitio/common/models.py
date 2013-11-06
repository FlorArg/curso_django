#!/usr/bin/env python
# -* encoding: utf8 *-

from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    MASCULINO = 'm'
    FEMENINO = 'f'
    SEXO_CHOICES = (
        (MASCULINO, 'Masculino'), (FEMENINO, 'Femenino')
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    
class Mascota(models.Model):
    # Constantes
    MACHO, HEMBRA = 'm', 'h'
    SEXO_CHOICES = (
        (MACHO, 'Macho'), (HEMBRA, 'Hembra')
    )
    duenio = models.ForeignKey(Persona, null=True, blank=True)
    raza = models.ForeignKey('Especie') # Relación hacia adelante
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

class Especie(models.Model):
    nombre = models.CharField(max_length=50)
    domesticable = models.BooleanField(default=True)

class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.ForeignKey(Especie)