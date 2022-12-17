from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class customer(models.Model):
    Nombre = models.ForeignKey(User, 
                on_delete=models.CASCADE,
                null = True,
                blank=True)
    Compania = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=15)
    CorreoE = models.EmailField(("Email"), max_length=254)

    def __str__(self):
        return self.Compania


class blog(models.Model):
    Autor = models.CharField(max_length=50)
    Titulo = models.CharField(max_length=100)
    Encabezado = models.CharField(max_length=400)
    Descripcion = models.TextField()
    Contenido = RichTextField()
    Imagen = models.URLField()
    Fecha = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return self.Titulo


