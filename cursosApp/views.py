from django.shortcuts import redirect, render
from .forms import cursoForm,estudianteForm,inscripcionForm

# Create your views here.
def newCurso(request):
    if request.method == 'POST':
        form = cursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = cursoForm()