from django.shortcuts import redirect, render,get_object_or_404
from .forms import cursoForm,estudianteForm,inscripcionForm
from .models import Curso, Estudiante, Inscripcion

# Create your views here.
#Cursos
def newCurso(request):
    if request.method == 'POST':
        form = cursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCursos')
    else:
        form = cursoForm()
    return render(request, 'cursos/newCurso.html', {'form': form})

def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listaCursos.html', {'cursos': cursos})

def detalleCurso(request,pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalle_curso.html', {'curso':curso})

def editarCurso(request,pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = cursoForm(request.POST,instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listarCursos')
    else:
        form = cursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})

def eliminarCurso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('listarCursos')
    else:
        return render(request, 'cursos/eliminarCurso.html', {'curso':curso})
        
#Estudiante
def newEstudiante(request):
    if request.method == 'POST':
        form = estudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarEstudiantes')
    else:
        form = estudianteForm()
    return render(request, 'cursos/newEstudiante.html', {'form': form})

def listarEstudiantes(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'cursos/listaEstudiantes.html', {'estudiante': estudiante})

def detalleCurso(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'cursos/detalle_estudiante.html', {'estudiante':estudiante})

def editarCurso(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = estudianteForm(request.POST,instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listarEstudiantes')
    else:
        form = estudianteForm(instance=estudiante)
    return render(request, 'cursos/editar_estudiante.html', {'form': form})

def eliminarCurso(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listarCursos')
    else:
        return render(request, 'cursos/eliminarEstudiante.html', {'curso':estudiante})