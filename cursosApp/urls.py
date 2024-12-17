from django.urls import path
from . import views

urlpatterns = [
    path('new/curso', views.newCurso, name='newCurso')
]
