#Encapsulacion en Python
class Prueba(object):
	#con dos __ bajos definimos una variable o metodo de tipo privado 
	def __init__(self):
		self.__privado ="Soy privado"
		self.privado = "Soy variable publico"

	def __metodoPrivado(self):
		return "Soy privado"

	def metodoPublico(self):
		print "Soy metodo publico"
     #con esta forma podemos mandar la variable privada
	def getPrivado(self):
		return self.__privado
	 #con set podemos mandar un nuevo valor
	def setPrivado(self,valor):
		self.__privado = valor
		#de esta forma podemos haceder al metodo
		self.__privado = self.__metodoPrivado()

obj = Prueba()

print obj.privado
obj.setPrivado('nuevo valor')
print obj.getPrivado()