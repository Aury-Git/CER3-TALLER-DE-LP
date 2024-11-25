from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Administrador_académico(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    key = models.CharField(max_length=40)

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.CharField(max_length=100)
    key = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre 


class PersonalServicio(models.Model):
    nombre = models.CharField(max_length=50)
    area_responsable = models.CharField(max_length=100)
    def __str__(self):
        return self.user.nombre 

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=100)
    key = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre 