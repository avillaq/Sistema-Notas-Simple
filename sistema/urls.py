from django.contrib import admin
from django.urls import path
from sistema import views 

urlpatterns = [
    path('', view=views.index, name='index'),
    path('crear_alumno/', view=views.crear_alumno, name='crear_alumno'),
    path('crear_curso/', view=views.crear_curso, name='crear_curso'),
    path('lista_alumnos/', view=views.lista_alumnos, name='lista_alumnos'),
    path('asignar_nota/<int:id_alumno>/', view=views.asignar_nota, name='asignar_nota'),
    path('guardar_nota/', view=views.guardar_nota, name='guardar_nota'),


]
