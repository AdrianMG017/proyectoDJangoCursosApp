from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10,unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class clean(self):
        if
