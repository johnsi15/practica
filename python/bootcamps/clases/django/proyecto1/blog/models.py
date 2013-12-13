from django.db import models

# Create your models here.

class Entrada(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.CharField(max_length=1000)
	fecha = models.DateTimeField('Fecha de publicacion')

class comentarios(models.Model):
	entrada = models.ForeignKey(Entrada)#relacionamos el comentario para saber a que entrada pertenece el comentario
	contenidoComentario = models.CharField(max_length=600)