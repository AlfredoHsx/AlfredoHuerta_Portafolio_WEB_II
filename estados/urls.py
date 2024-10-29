from django.urls import path
from .views import cargar_estados, cargar_municipios

urlpatterns = [
    path('', cargar_estados, name='cargar_estados'),
    path('municipios/', cargar_municipios, name='cargar_municipios'),
]
