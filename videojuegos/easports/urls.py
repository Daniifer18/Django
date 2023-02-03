from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= "easport raiz"),
    path('<str:nombre>/',views.detalle_equipo,name="easports detalle_equipo"),
    path('juego/<str:nombre>/',views.detalle_juego,name="easports detalle_juego"),
    path('genero/<str:nombre>/',views.detalle_genero,name="easports detalle_genero"),
]
