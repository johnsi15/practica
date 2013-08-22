#CLASES DECORADORES PARTE DOS
#def decorador(funcion):
#	def funcionDecorador(*args,**kwargs):
#		print "Funcion ejecutada ", funcion.__name__
#		funcion(*args,**kwargs)

#	return funcionDecorador
class Decorador(object):
	"""Mi clase decorador"""
	def __init__(self, funcion):
		self.funcion = funcion
	#con el call es como si fuera funcionDecorador ok
	def __call__(self,*args,**kwargs):
		print "Funcion ejecutada ", self.funcion.__name__
		self.funcion(*args,**kwargs)

@Decorador
def resta(a,b):
	print a-b

resta(5,3)

