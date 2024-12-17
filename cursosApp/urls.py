from django.urls import path
from . import views

urlpatterns = [
    path('curso/lista', views.listarCursos, name='listarCursos'),
    path('curso/nuevo', views.newCurso, name='newCurso'),
    path('curso/detalle/<int:pk>', views.detalleCurso, name='detalleCurso'),
    path('curso/editar/<int:pk>', views.editarCurso, name='editarCurso'),
    path('curso/eliminar/<int:pk>', views.eliminarCurso, name='eliminarCurso'),
    path('estudiante/lista', views.listarEstudiantes, name='listarEstudiantes'),
    path('estudiante/nuevo', views.newEstudiante, name='newEstudiante'),
    path('estudiante/detalle/<int:pk>', views.detalleEstudiante, name='detalleEstudiante'),
    path('estudiante/editar/<int:pk>', views.editarEstudiante, name='editarEstudiante'),
    path('estudiante/eliminar/<int:pk>', views.eliminarEstudiante, name='eliminarEstudiante'),
    path('inscripcion/lista', views.listarInscripcion, name='listarInscripcion'),
    path('inscripcion/nuevo', views.newInscripcion, name='newInscripcion'),
    path('inscripcion/detalle/<int:pk>', views.detalleInscripcion, name='detalleInscripcion'),
    path('inscripcion/eliminar/<int:pk>', views.eliminarInscripcion, name='eliminarInscripcion'),
]
