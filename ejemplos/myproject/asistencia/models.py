from django.db import models

# Create your models here.
class EntradaDeAsistencia(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now=True)