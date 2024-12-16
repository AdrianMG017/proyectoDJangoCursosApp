from django import forms
from . import models
from django.core.exceptions import ValidationError
from datetime import date

class cursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = '__all__'
        widgets = {
                'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
                'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            }
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio > fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser mayor a la fecha final.")
        return cleaned_data