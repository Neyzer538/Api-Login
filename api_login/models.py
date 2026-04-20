from django.db import models
from .validators import evaluar_contrasenia

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    estado = models.BooleanField()
    fechaMod = models.DateTimeField(auto_now_add=True)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    contrasenia = models.CharField(max_length=128)
    estado = models.BooleanField()
    fechaMod = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios')
    
    def __str__(self):
        return self.nombre