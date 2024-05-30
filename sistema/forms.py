from django import forms 
from .models import Alumno, Curso, NotasAlumnosPorCurso
# creating a form 
class CursoForm(forms.Form): 
    nombre_curso = forms.CharField(max_length=30, label='Nombre del curso') 

    class Meta:
        model = Curso
        fields = ['nombre_curso']

class AlumnoForm(forms.Form):
    nombre_alumno = forms.CharField(max_length=30, label='Nombre del alumno')
    apellido_alumno = forms.CharField(max_length=30, label='Apellidos del alumno')

    class Meta:
        model = Alumno
        fields = ['nombre_alumno', 'apellido_alumno']
