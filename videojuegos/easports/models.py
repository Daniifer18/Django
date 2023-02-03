from django.db import models

# Create your models here.

class Equipo(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    annio = models.DateField()
    foto = models.ImageField(upload_to="videojuegos/media",null= True)
    
    def __str__(self):
        return f"{self.nombre} ({self.annio})"


class Genero(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} ({self.descripcion})"

class Juego(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    annio = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    equipos = models.ManyToManyField(Equipo, related_name= "juego")
    
    def __str__(self):
        return f"{self.nombre} [{self.genero}]({self.annio})"