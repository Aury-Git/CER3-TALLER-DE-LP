from django.shortcuts import render
import requests


from rest_framework.views import APIView
from rest_framework.response import Response
from api import models

from api import serializers

from django.http import JsonResponse




#def inicio(request):
#    productos = models.Producto.objects.all()
#    data = {
#        'productos':productos,
#    return render(request, 'index.html',data)
#    }

def feriados():
    # Datos de la API de terceros
    headers = {
        "User-Agent": "EduPlanner/1.0"
    }
    info = requests.get("https://apis.digital.gob.cl/fl/feriados/2024", headers=headers)
    info.raise_for_status()
    return info.json()
    '''
    feriados = info.json()

    data = {
        "titulo":titulo,
        "feriados":feriados,
    }

    return render(request,'calendario.html',data)
    '''

    ''''
    lista_feriados = list()

    for p in feriados:
        feriado = Feriado(
            nombre = p["nombre"],
            fecha = p["fecha"],
            tipo = p["tipo"],
        )
    
        lista_feriados.append(feriado)
    '''
def datos_en_json(request):
    # Datos de los dias feriados
    dias_feriados = feriados()

    # Datos de mi Api 
    actividades = list(models.Actividades.objects.values("titulo", "descripcion", "inicio","fin","tipo",))
    #actividades = models.Actividades.objects.all()
    #serializera = serializer.ActividadesSerializer(actividades, many=True)
    datos_combinados = {
        "actividades": actividades,
        "feriados": dias_feriados,
    }
    return JsonResponse(datos_combinados)

def datos_graficos(request):
    # Datos de los dias feriados
    dias_feriados = feriados()

    # Datos de mi Api 
    actividades = list(models.Actividades.objects.values("titulo", "descripcion", "inicio","fin","tipo",))
    #actividades = models.Actividades.objects.all()
    #serializera = serializer.ActividadesSerializer(actividades, many=True)
    data = {
        "actividades": actividades,
        "feriados": dias_feriados,
    }

    # Renderiza los datos en la plantilla HTML
    return render(request, 'calendario.html', data)