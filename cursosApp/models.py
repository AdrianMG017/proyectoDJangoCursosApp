from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10,unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser mayor a la fecha final.")
        return super().clean()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.CharField()

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser posterior a la fecha actual.")
        if date.today().year - self.fecha_nacimiento.year < 18:
            raise ValidationError("Debes de tener mayoria de edad.")
        return super().clean()
        
class Incripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    fecha_inscripcion = models.CharField()

    def clean(self):
        if self.curso.fecha_fin < self.fecha_inscripcion:
            raise ValidationError("No te puedes  inscribir en un curso ya finalizado.")
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de no puede ser posterior al día actual.")
        return super().clean()
