from django.shortcuts import redirect, render,get_object_or_404
from .forms import cursoForm,estudianteForm,inscripcionForm, flitrarInscripcionForms
from .models import Curso, Estudiante, Inscripcion
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#Cursos
class ListarCurso(LoginRequiredMixin,ListView):
    model = Curso
    template_name = 'cursos/listaCursos.html'
    context_object_name = "cursos"

class CrearCurso(CreateView):
    model =Curso
    template_name = 'cursos/newCurso.html'
    form_class = cursoForm
    success_url = reverse_lazy('listarCursos')
    
class EditarCurso(UpdateView):
    model = Curso
    template_name = 'cursos/editar_curso.html'
    form_class = cursoForm
    success_url = reverse_lazy('listarCursos')
    
class DeleteCurso(DeleteView):
    model = Curso
    template_name = 'cursos/eliminarCurso.html'
    success_url = reverse_lazy('listarCursos')
    

# def newCurso(request):
#     if request.method == 'POST':
#         form = cursoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listarCursos')
#     else:
#         form = cursoForm()
#     return render(request, 'cursos/newCurso.html', {'form': form})

# def listarCursos(request):
#     cursos = Curso.objects.all()
#     return render(request, 'cursos/listaCursos.html', {'cursos': cursos})

def detalleCurso(request,pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/detalle_curso.html', {'curso':curso})

# def editarCurso(request,pk):
#     curso = get_object_or_404(Curso, pk=pk)
#     if request.method == 'POST':
#         form = cursoForm(request.POST,instance=curso)
#         if form.is_valid():
#             form.save()
#             return redirect('listarCursos')
#     else:
#         form = cursoForm(instance=curso)
#     return render(request, 'cursos/editar_curso.html', {'form': form})

# def eliminarCurso(request, pk):
#     curso = get_object_or_404(Curso, pk=pk)
#     if request.method == 'POST':
#         curso.delete()
#         return redirect('listarCursos')
#     else:
#         return render(request, 'cursos/eliminarCurso.html', {'curso':curso})
        
#Estudiante
class ListarEstudiante(ListView):
    model = Estudiante
    template_name = 'cursos/listaEstudiantes.html'
    context_object_name = "estudiantes"

class CrearEstudiante(CreateView):
    model = Estudiante
    template_name = 'cursos/newEstudiante.html'
    form_class = estudianteForm
    success_url = reverse_lazy('listarEstudiantes')
    
class EditarEstudiante(UpdateView):
    model = Estudiante
    template_name = 'cursos/editar_estudiante.html'
    form_class = estudianteForm
    success_url = reverse_lazy('listarEstudiantes')
    
class DeleteEstudiante(DeleteView):
    model = Estudiante
    template_name = 'cursos/eliminarEstudiante.html'
    success_url = reverse_lazy('listarEstudiantes')

# def newEstudiante(request):
#     if request.method == 'POST':
#         form = estudianteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listarEstudiantes')
#     else:
#         form = estudianteForm()
#     return render(request, 'cursos/newEstudiante.html', {'form': form})

# def listarEstudiantes(request):
#     estudiantes = Estudiante.objects.all()
#     return render(request, 'cursos/listaEstudiantes.html', {'estudiantes': estudiantes})

def detalleEstudiante(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'cursos/detalle_estudiante.html', {'estudiante':estudiante})

# def editarEstudiante(request,pk):
#     estudiante = get_object_or_404(Estudiante, pk=pk)
#     if request.method == 'POST':
#         form = estudianteForm(request.POST,instance=estudiante)
#         if form.is_valid():
#             form.save()
#             return redirect('listarEstudiantes')
#     else:
#         form = estudianteForm(instance=estudiante)
#     return render(request, 'cursos/editar_estudiante.html', {'form': form})

# def eliminarEstudiante(request, pk):
#     estudiante = get_object_or_404(Estudiante, pk=pk)
#     if request.method == 'POST':
#         estudiante.delete()
#         return redirect('listarEstudiantes')
#     else:
#         return render(request, 'cursos/eliminarEstudiante.html', {'estudiante':estudiante})
    

#Inscripcion
class ListarInscripcion(ListView):
    model = Inscripcion
    template_name = 'cursos/listaInscripciones.html'
    context_object_name = "inscripciones"

class CrearInscripcion(CreateView):
    model = Inscripcion
    template_name = 'cursos/newInscripcion.html'
    form_class = inscripcionForm
    success_url = reverse_lazy('listarInscripcion')
    
class EditarInscripcion(UpdateView):
    model = Inscripcion
    template_name = 'cursos/editar_inscripcion.html'
    form_class = inscripcionForm
    success_url = reverse_lazy('listarInscripcion')
    
class DeleteInscripcion(DeleteView):
    model = Inscripcion
    template_name = 'cursos/eliminarInscripcion.html'
    success_url = reverse_lazy('listarInscripcion')

# def newInscripcion(request):
#     if request.method == 'POST':
#         form = inscripcionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listarInscripcion')
#     else:
#         form = inscripcionForm()
#     return render(request, 'cursos/newInscripcion.html', {'form': form})

# def listarInscripcion(request):
#     inscripciones = Inscripcion.objects.all()
#     return render(request, 'cursos/listaInscripciones.html', {'inscripciones': inscripciones})

def detalleInscripcion(request,pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    return render(request, 'cursos/detalle_inscripcion.html', {'inscripcion':inscripcion})

# def eliminarInscripcion(request, pk):
#     inscripcion = get_object_or_404(Inscripcion, pk=pk)
#     if request.method == 'POST':
#         inscripcion.delete()
#         return redirect('listarInscripcion')
#     else:
#         return render(request, 'cursos/eliminarInscripcion.html', {'inscripcion':inscripcion})