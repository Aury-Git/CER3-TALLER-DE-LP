from . import models
from rest_framework import routers, serializers

class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Actividad
        fields = '__all__'
        # fields = ["nombre", "duracion", "jefe_carrera"]
        #exclude = ['codigo']