from django import forms 
from .models import Alumno, Curso, NotasAlumnosPorCurso
# creating a form 
class CursoForm(forms.ModelForm): 
    nombre_curso = forms.CharField(max_length=30, label='Nombre del curso') 

    class Meta:
        model = Curso
        fields = ['nombre_curso']
    
    def save(self, commit=True):
        nombre_curso = self.cleaned_data.get('nombre_curso')
        curso, estado = Curso.objects.get_or_create(nombre_curso=nombre_curso)
        if commit:
            curso.save()
        return curso

class AlumnoForm(forms.ModelForm):
    nombre_alumno = forms.CharField(max_length=30, label='Nombre del alumno')
    apellido_alumno = forms.CharField(max_length=30, label='Apellidos del alumno')
    cursos = forms.ModelMultipleChoiceField(queryset=Curso.objects.all(), label='Cursos')

    class Meta:
        model = Alumno
        fields = ['nombre_alumno', 'apellido_alumno', 'cursos']

    def save(self, commit=True):
        nombre_alumno = self.cleaned_data.get('nombre_alumno')
        apellido_alumno = self.cleaned_data.get('apellido_alumno')
        cursos = self.cleaned_data.get('cursos')
        alumno, estado = Alumno.objects.get_or_create(nombre_alumno=nombre_alumno, apellido_alumno=apellido_alumno)
        for curso in cursos:
            NotasAlumnosPorCurso.objects.get_or_create(id_alumno=alumno, id_curso=curso)
        if commit:
            alumno.save()
        return alumno
