from django.db import models


# Create your models here.

class Puesto(models.Model):
    puestos=models.CharField(max_length=50)

class Integrante(models.Model):
    puesto_integrante=models.OneToOneField(Puesto,verbose_name='Puesto', on_delete=models.CASCADE)
    nombre_integrante=models.CharField(max_length=50)

class MisionVision(models.Model):
    mision=models.TextField()
    vision=models.TextField()
