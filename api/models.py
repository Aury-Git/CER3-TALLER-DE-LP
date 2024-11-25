from django.db import models

# Create your models here.

class Actividades(models.Model):
    TIPO_EVENTO = [
        ('inicio_semestre', 'Inicio de Semestre'),
        ('fin_semestre', 'Fin de Semestre'),
        ('inicio_de_inscripcion_de_asignaturas', 'Inicio de Inscripción de Asignaturas'),
        ('fin_de_inscripcion_de_asignaturas', 'Fin de Inscripción de Asignaturas'),
        ('receso_academico', 'Receso Académico'),
        ('feriado_nacional', 'Feriado Nacional'),
        ('feriado_regional', 'Feriado Regional'),
        ('inicio_de_plazos_de_solicitudes_administrativas', 'Inicio de Plazos de Solicitudes Administrativas'),
        ('fin_de_plazos_de_solicitudes_administrativas', 'Fin de Plazos de Solicitudes Administrativas'),
        ('inicio_de_plazos_para_la_gestión_de_beneficios', 'Inicio de Plazos para la Gestión de Beneficios'),
        ('fin_de_plazos_para_la_gestión_de_beneficios', 'Fin de Plazos para la Gestión de Beneficios'),
        ('ceremonia_de_titulación_o_graduación', 'Ceremonia de Titulación o Graduación'),
        ('reunión_de_consejo_académico', 'Reunión de Consejo Académico'),
        ('talleres_y_charlas', 'talleres y charlas'),
        ('dia_de_Orientacion_para_nuevos_estudiantes', 'Día de Orientación para Nuevos Estudiantes'),
        ('eventos_extracurriculares', 'Eventos Extracurriculares'),
        ('inicio_de_clases', 'Inicio de Clases'),
        ('ultimo_dia_de_clases', 'Último Día de Clases'),
        ('dia_de_puertas_abiertas', 'Día de Puertas Abiertas'),
        ('suspensión_de_actividades_completa', 'Suspensión de Actividades Completa'),
        ('suspensión_de_actividades_pparcial', 'Suspensión de Actividades Parcial'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(default="Sin descripcion")
    inicio = models.DateField()
    fin = models.DateField()
    tipo = models.CharField(max_length=100, choices=TIPO_EVENTO)

    nombre = str(titulo) +" "+ str(tipo)  

    def __str__(self):
        return nombre  
    
    

# para hacer la migraciones de los modelos

#  python manage.py migrate
#  python manage.py makemigrations

