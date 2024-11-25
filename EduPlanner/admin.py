from django.contrib import admin

from .models import Docente, PersonalServicio, Estudiante, Administrador_académico

admin.site.register(Administrador_académico)
admin.site.register(Docente)
admin.site.register(PersonalServicio)
admin.site.register(Estudiante)

# Register your models here.
