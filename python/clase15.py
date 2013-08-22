#HERENCIAS MULTIPLES......
class Humano:
	def __init__(self):
		#self.edad = edad #creamos un atributo con selft.edad
		print 'hola'
		
	def hablar(self,mensaje):
		print mensaje
		
#heredamos de la clase Humano sus metodos como asi-> ()
class IngSistemas(Humano):
	def __init__(self):
		print 'Hola'

	def programar(self,lenguaje):
		print 'Voy a programar en ',lenguaje

class LicDerecho(Humano):
	def estCaso(self,de):
		print 'Debo de estudiar el caso de ',de

class estudioso(IngSistemas,LicDerecho):#tener en cuenta el orden de llamado si hay un __init__
	pass #colocamos la palabra reservada pass si no vamoa a definir metodos

pepe = estudioso()

pepe.hablar('Hola soy de herencia multiple')

pepe.programar('python')

pepe.estCaso('Andrey')