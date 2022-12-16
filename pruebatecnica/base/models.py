from django.db import models
from django.contrib.auth.models import User


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


