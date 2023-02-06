from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticia

# Create your views here.


def index (request):
    return HttpResponse("Estas en el index de las noticias")


def detalle_noticia (request,id):
    noticia = Noticia.objects.get(id = id)
    context = {'noticia': noticia}
    return render (request,'base.html', context)
    

