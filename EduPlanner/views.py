from django.shortcuts import render
import requests


def Feriados(request):
    titulo = "Feriados"

    info = requests.get("https://apis.digital.gob.cl/fl/feriados/2024")
    feriados = info.json()

    lista_feriados = list()

    for p in feriados:
        feriados = Feriados(
        nombre = p["nombre"],
        fecha = p["fecha"],
        tipo = p["tipo"]
        )

        lista_feriados.append(feriados)

    
    data = {
        "titulo":titulo,
        "feriados":lista_feriados,
    }

    return render(request,'C3_Eduplanner/calendario.html',data)