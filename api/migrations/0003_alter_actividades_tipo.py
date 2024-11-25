# Generated by Django 5.1.3 on 2024-11-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_actividades_descripcion_alter_actividades_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='tipo',
            field=models.CharField(choices=[('inicio_semestre', 'Inicio de Semestre'), ('fin_semestre', 'Fin de Semestre'), ('inicio_de_inscripcion_de_asignaturas', 'Inicio de Inscripción de Asignaturas'), ('fin_de_inscripcion_de_asignaturas', 'Fin de Inscripción de Asignaturas'), ('receso_academico', 'Receso Académico'), ('feriado_nacional', 'Feriado Nacional'), ('feriado_regional', 'Feriado Regional'), ('inicio_de_plazos_de_solicitudes_administrativas', 'Inicio de Plazos de Solicitudes Administrativas'), ('fin_de_plazos_de_solicitudes_administrativas', 'Fin de Plazos de Solicitudes Administrativas'), ('inicio_de_plazos_para_la_gestión_de_beneficios', 'Inicio de Plazos para la Gestión de Beneficios'), ('fin_de_plazos_para_la_gestión_de_beneficios', 'Fin de Plazos para la Gestión de Beneficios'), ('ceremonia_de_titulación_o_graduación', 'Ceremonia de Titulación o Graduación'), ('reunión_de_consejo_académico', 'Reunión de Consejo Académico'), ('talleres_y_charlas', 'talleres y charlas'), ('dia_de_Orientacion_para_nuevos_estudiantes', 'Día de Orientación para Nuevos Estudiantes'), ('eventos_extracurriculares', 'Eventos Extracurriculares'), ('inicio_de_clases', 'Inicio de Clases'), ('ultimo_dia_de_clases', 'Último Día de Clases'), ('dia_de_puertas_abiertas', 'Día de Puertas Abiertas'), ('suspensión_de_actividades_completa', 'Suspensión de Actividades Completa'), ('suspensión_de_actividades_pparcial', 'Suspensión de Actividades Parcial')], max_length=100),
        ),
    ]
