#FUNCIONES DE ORDEN SUPERIOR
def prueba(f):
	#con los f() indicamos que se trata de una funcion
	return f()

def porEnviar():
	return 2+2

print prueba(porEnviar)

#____________________________#
def seleccion(operacion):
	def suma(a,b):
		return a+b

	def multiplicacion(a,b):
		return a*b

	if operacion == "suma":
		return suma
	elif operacion == "multi":
		return multiplicacion

fGuardada = seleccion('suma')
fGuardada2 = seleccion('multi')
print fGuardada(3,4)
print fGuardada2(4,4)
