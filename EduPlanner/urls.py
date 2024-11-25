from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.datos_graficos, name='home'), 
    path('json/', views.datos_en_json, name='json'), 
]

    
