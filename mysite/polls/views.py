from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def saludo(request):
    return HttpResponse("Hola, como estas.")

def navegador(request):
    return HttpResponse("Estas usando el navegador:"+request.META["HTTP_USER_AGENT"])
