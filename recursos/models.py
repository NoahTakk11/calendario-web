from django.db import models

class Recursos(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Título')
    descripcion=models.CharField(max_length=250, verbose_name='Descripción')
    url=models.URLField(verbose_name='Link de acceso')

    def __str__(self):
        return f'{self.titulo} {self.descripcion} {self.url}'
