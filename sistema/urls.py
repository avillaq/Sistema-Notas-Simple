from django.contrib import admin
from django.urls import path
from sistema import views 

urlpatterns = [
    path('', view=views.index, name='index'),
    path('crear_alumno/', view=views.crear_alumno, name='crear_alumno'),
    path('crear_curso/', view=views.crear_curso, name='crear_curso'),
    path('asignar_notas/', view=views.asignar_notas, name='asignar_notas'),

]
