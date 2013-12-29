from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=150) # varchar(150)
	descripcion = models.TextField()
	precio = models.IntegerField()

	def __unicode__(self):
		return self.nombre