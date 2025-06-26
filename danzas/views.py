from django.shortcuts import render
from .models import DanzaEstilo #importo la el modelo DanzaEstilo para leer datos de la base de datos

def lista_estilos(request): 
    #se ejecuta cuando alguien entre a una URL
    estilos = DanzaEstilo.objects.all() 
    #Le pedimos a Django que consulte la base de datos y traiga todos los objetos del modelo DanzaEstilo
    return render(request, "danzas/lista_estilos.html", {"estilos": estilos})
    #Le decimos a Django: “usá el template danzas/lista_estilos.html y pasale los datos estilos”