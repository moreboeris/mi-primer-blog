from django.urls import path
from . import views #Importás el archivo views.py de tu propia app

urlpatterns = [
    path('evaluacion2', views.lista_estilos, name="lista_estilos"), #la función path, que sirve para definir rutas/URLs
]