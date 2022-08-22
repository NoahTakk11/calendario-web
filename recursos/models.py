from django.db import models

class Recursos(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=250)
    url=models.URLField()

    def __str__(self):
        return f'{self.titulo} {self.descripcion} {self.url}'
