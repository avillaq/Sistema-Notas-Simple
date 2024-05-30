from django.shortcuts import render , redirect
from .forms import CursoForm, AlumnoForm
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

def asignar_notas(request):
    return render(request, 'asignar_notas.html')