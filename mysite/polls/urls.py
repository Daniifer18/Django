from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludo/', views.saludo, name='saludo'),
    path('navegador/', views.navegador, name='navegador'),
]