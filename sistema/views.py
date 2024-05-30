from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def crear_alumno(request):
    return render(request, 'crearAlumno.html')

def crear_curso(request):
    return render(request, 'crearCurso.html')

def asignar_notas(request):
    return render(request, 'AsignarNotas.html')