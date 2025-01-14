from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User
 
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10,unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuario = models.ForeignKey(User)

    class Meta():
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.codigo} - {self.nombre}' 
    
    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser mayor a la fecha final.")
        return super().clean()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    class Meta():
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser posterior a la fecha actual.")
        edad=(date.today() - self.fecha_nacimiento).days // 365
        if edad < 18:
            raise ValidationError("Debes de tener mayoria de edad.")
        return super().clean()
        
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()

    class Meta():
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return f'{self.curso.nombre} - {self.estudiante.nombre} - {self.fecha_inscripcion}'

    def clean(self):
        if self.curso.fecha_fin < self.fecha_inscripcion:
            raise ValidationError("No te puedes  inscribir en un curso ya finalizado.")
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de no puede ser posterior al día actual.")
        if Inscripcion.objects.filter(estudiante=self.estudiante, curso=self.curso).exclude(pk=self.pk).exists():
            raise ValidationError("Este estudiante ya está inscrito en este curso")
        return super().clean()
