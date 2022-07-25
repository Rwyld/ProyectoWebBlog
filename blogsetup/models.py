import email
from pickle import TRUE
from ssl import create_default_context
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=TRUE)
    update = models.DateTimeField(auto_now_add=TRUE)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre


class Contenido(models.Model):
    titulo = models.CharField("Titulo", max_length=50)
    subtitulo = models.CharField("Subtitulo", max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to = 'media')
    texto = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=TRUE)
    update = models.DateTimeField(auto_now_add=TRUE)

class Registro(models.Model):
    usuario = models.CharField("Usuario", max_length=20)
    contraseña = models.CharField("Contraseña", max_length=10)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=TRUE)
    update = models.DateTimeField(auto_now_add=TRUE)


class Contacto(models.Model):
    nombre = models.CharField("Nombre", max_length=20)
    asunto = models.CharField("Asunto", max_length=40, null=TRUE)
    email = models.EmailField()
    mensaje = models.CharField("Mensaje", max_length=500)
    created = models.DateTimeField(auto_now_add=TRUE)
    update = models.DateTimeField(auto_now_add=TRUE)


class DiseñoWeb(models.Model):
    imagen = models.ImageField(upload_to = 'WebMedia')