from django.db import models
from django.utils import timezone

# Create your models here.

class Mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField(blank=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Demo(models.Model):
    nombre = models.CharField(max_length=100)
    url_pag = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    url_foto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
