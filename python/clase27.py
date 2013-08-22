#DECORADORES.....
loggeado = True
usuario = 'Andrey'

def admin(f):
	def comprobar(*args,**kwargs):
		if loggeado:
			f(*args,**kwargs)
		else:
			print "No tiene permisos para ejecutar esta funcion", f.__name__
	return comprobar

def decorador(funcion):
	def funcionDecorador(*args,**kwargs):
		print "Funcion ejecutada ", funcion.__name__
		funcion(*args,**kwargs)

	return funcionDecorador
#colocando @ le estamos diciendo a python que se trata de un decorador
@admin
def resta(a,b):
	print a-b

resta(5,2)
#decorador
#resta(5,3)
#decorador(resta)(8,4)