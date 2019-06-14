from django.db import models
from django.urls import reverse

# Create your models here.

class Pais(models.Model):
    abreviacion = models.CharField(max_length=2, help_text="Ingrese la abreviacion")
    nombre = models.CharField(max_length=50, help_text="Ingrese el pais")
    codigo = models.CharField(max_length=50, help_text="Ingrese codigo telefonico")

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('cliente:listar-pais')