from django.shortcuts import render , redirect
from .forms import CursoForm, AlumnoForm
from .models import Alumno, NotasAlumnosPorCurso
# Create your views here.
def index(request):
    return render(request, 'index.html')

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'crear_alumno.html', {'form': form})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

def asignar_nota(request, id_alumno):
    cursos = NotasAlumnosPorCurso.objects.filter(id_alumno=id_alumno)
    return render(request, 'asignar_notas.html', {'alumno': id_alumno, 'cursos': cursos})