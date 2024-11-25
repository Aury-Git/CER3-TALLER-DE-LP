from django.shortcuts import render
from rest_framework import viewsets
from . import serializers # De aqui vienen los datos
from . import models

class ActividadesViewSet(viewsets.ModelViewSet):
    queryset = models.Actividades.objects.all()
    serializer_class = serializers.ActividadesSerializer

# Create your views here.

