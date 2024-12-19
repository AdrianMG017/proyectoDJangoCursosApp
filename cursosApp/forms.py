from django import forms
from . import models
from django.core.exceptions import ValidationError
from datetime import date

class cursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = '__all__'
        widgets = {
                'fecha_inicio': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
                'fecha_fin': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            }
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio > fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser mayor a la fecha final.")
        return cleaned_data

class estudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = '__all__'
        widgets = {
                'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'})
    }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        if models.Estudiante.objects.filter(email=email).exists():
            raise ValidationError("El email ya esta en uso.")
        edad=(date.today() - fecha_nacimiento).days // 365
        if edad < 18:
            raise ValidationError("Debes de tener mayoria de edad.")
        return cleaned_data

class inscripcionForm(forms.ModelForm):
    class Meta:
        model = models.Inscripcion
        fields = '__all__'
        widgets = {
                'fecha_inscripcion': forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'})
    }

    def clean(self):
        cleaned_data = super().clean()
        curso = cleaned_data.get('curso')
        fecha_inscripcion = cleaned_data.get('fecha_inscripcion')
        if curso.fecha_fin < fecha_inscripcion:
            raise ValidationError("No te puedes  inscribir en un curso ya finalizado.")
        if fecha_inscripcion > date.today():
            raise ValidationError("La fecha de no puede ser posterior al día actual.")
        return cleaned_data
    
class flitrarInscripcionForms(forms.ModelForm):
    model =models.Inscripcion
    fields = ['estudiante','curso']