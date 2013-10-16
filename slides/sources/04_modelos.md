# Modelos

Cada aplicación tiene un archivo models.py
donde se definen lo modelos

    !python

    from django.db import models

    class Persona(models.Model):
        nombre = models.CharField(max_length=50)

    class Auto(models.Model):
        patente = models.CharField(max_length=50)

# Sincronización de la base de datos
