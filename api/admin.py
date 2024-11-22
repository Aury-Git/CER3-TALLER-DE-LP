from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Actividades)

# python manage.py createsuperuser
# user: admin
# correo: admin@gmail.com
# pass: admin