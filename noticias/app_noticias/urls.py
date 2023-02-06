from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= "noticia raiz"),
    path('<int:id>/',views.detalle_noticia,name="noticias detalle_noticia"),
]