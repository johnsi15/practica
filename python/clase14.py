#HERENCIAS......
class Humano:
	def __init__(self,edad):
		self.edad = edad #creamos un atributo con selft.edad
		
	def hablar(self,mensaje):
		print mensaje
		
#heredamos de la clase Humano sus metodos como asi ()
class IngSistemas(Humano):
	def programar(self,lenguaje):
		print 'Voy a programar en ',lenguaje

class LicDerecho(Humano):
	def estCaso(self,de):
		print 'Debo de estudiar el caso de ',de

pedro = IngSistemas(25)
john = LicDerecho(20)

pedro.programar('python')
john.estCaso('pedro')

pedro.hablar("Hola....")
john.hablar("Joder como vamos....")
