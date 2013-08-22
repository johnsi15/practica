from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	usuario = models.ForeignKey(User)#llave foranea
	nombre = models.CharField(max_length=100, unique=True)
	categoria = models.ForeignKey(Categoria)#llave foranea 
	descripcion = models.TextField()
	disponible = models.BooleanField(default = True)

	def __unicode__(self):
		return self.nombre
