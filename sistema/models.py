from django.db import models

# Create your models here.

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre_alumno = models.CharField(max_length=30)
    apellido_alumno = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_alumno

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_curso
    
class NotasAlumnosPorCurso(models.Model):
    id_notas= models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota1 = models.PositiveBigIntegerField(blank=True, null=True)
    nota2 = models.PositiveBigIntegerField(blank=True, null=True)
    nota3 = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id_alumno.nombre_alumno} {self.id_curso.nombre_curso}"