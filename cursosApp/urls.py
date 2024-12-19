from django.urls import path
from . import views

urlpatterns = [
    #path('curso/lista', views.listarCursos, name='listarCursos'),
    path('curso/lista', views.ListarCurso.as_view(), name='listarCursos'),
    #path('curso/nuevo', views.newCurso, name='newCurso'),
    path('curso/nuevo', views.CrearCurso.as_view(), name='newCurso'),
    path('curso/detalle/<int:pk>', views.detalleCurso, name='detalleCurso'),
    #path('curso/editar/<int:pk>', views.editarCurso, name='editarCurso'),
    path('curso/editar/<int:pk>', views.EditarCurso.as_view(), name='editarCurso'),
    #path('curso/eliminar/<int:pk>', views.eliminarCurso, name='eliminarCurso'),
    path('curso/eliminar/<int:pk>', views.DeleteCurso.as_view(), name='eliminarCurso'),
    path('estudiante/lista', views.ListarEstudiante.as_view(), name='listarEstudiantes'),
    path('estudiante/nuevo', views.CrearEstudiante.as_view(), name='newEstudiante'),
    path('estudiante/detalle/<int:pk>', views.detalleEstudiante, name='detalleEstudiante'),
    path('estudiante/editar/<int:pk>', views.EditarEstudiante.as_view(), name='editarEstudiante'),
    path('estudiante/eliminar/<int:pk>', views.DeleteEstudiante.as_view(), name='eliminarEstudiante'),
    path('inscripcion/lista', views.ListarInscripcion.as_view(), name='listarInscripcion'),
    path('inscripcion/nuevo', views.CrearInscripcion.as_view(), name='newInscripcion'),
    path('inscripcion/editar/<int:pk>', views.EditarInscripcion.as_view(), name='editarInscripcion'),
    path('inscripcion/detalle/<int:pk>', views.detalleInscripcion, name='detalleInscripcion'),
    path('inscripcion/eliminar/<int:pk>', views.DeleteCurso.as_view(), name='eliminarInscripcion'),
]
