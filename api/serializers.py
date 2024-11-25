from rest_framework import routers, serializers
from . import models

# Para transformar los datos de las clases a JSON 

class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Actividades
        fields = '__all__'
        # fields = ["nombre", "duracion", "jefe_carrera"]
        #exclude = ['codigo']