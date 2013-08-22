#clases y metodos
class Humano:
	def __init__(self,edad):
		self.edad = edad #creamos un atributo con selft.edad
		
	def hablar(self,mensaje):
		print self.edad #podemos tambien aceder al atributo 
		print mensaje

pedro = Humano(25)
john = Humano(20)

print "Hola soy pedro tengo ",pedro.edad
print "hola soy john tengo ",john.edad

pedro.hablar("Hola....")

john.hablar("Joder como vamos....")
