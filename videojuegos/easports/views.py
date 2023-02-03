from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo , Juego , Genero

# Create your views here.


def index (request):
    return HttpResponse("Estas en el index de easports")


def detalle_equipo (request,nombre):
    equipo = Equipo.objects.get(nombre = nombre)
    context = {'equipo': equipo}
    return render (request,'easports/equipo.html', context)

def detalle_juego (request,nombre):
    return HttpResponse(f"El nombre del juego es {nombre}")

def detalle_genero (request,nombre):
    return HttpResponse(f"El genero es {nombre}")