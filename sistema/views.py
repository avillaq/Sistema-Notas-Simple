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
    return render(request, 'asignar_notas.html', {'id_alumno': id_alumno, 'cursos': cursos})

def guardar_nota(request):
    id_alumno = request.POST.get('id_alumno')
    id_curso = request.POST.get('id_curso')
    nota1 = request.POST.get('nota1')
    nota2 = request.POST.get('nota2')
    nota3 = request.POST.get('nota3')
    notas, estado = NotasAlumnosPorCurso.objects.get_or_create(id_alumno_id=id_alumno, id_curso_id=id_curso)
    notas.nota1 = nota1
    notas.nota2 = nota2
    notas.nota3 = nota3
    notas.save()
    return redirect('index')