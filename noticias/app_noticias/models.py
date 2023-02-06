from django.db import models

# Create your models here.

class Noticia(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto1 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto2 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto3 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto4 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto5 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    
    def __str__(self):
        return f"{self.titulo} ({self.descripcion})"
