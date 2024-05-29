from django.db import models

# Create your models here.

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre_alumno = models.CharField(max_length=30)
    apellido_alumno = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_alumno