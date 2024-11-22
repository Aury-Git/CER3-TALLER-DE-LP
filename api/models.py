from django.db import models

# Create your models here.

class Actividades(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=200)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    

# para hacer la migraciones de los modelos

#  python manage.py migrate
#  python manage.py makemigrations

