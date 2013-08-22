#Funciones en Python....
#con def definimos la funcion......
def suma(num1, num2):
	suma = num1 + num2
	print "La suma de los Numeros es: "+ str(suma)

#ejecutamos la funcion suma....
suma(5,4)

#con un * indicamos que es una tupla con ** que es un diccionario
def funcion(cad, v=2,**algomas):
	print cad * v
	print algomas['cadenaextra']#de esta forma entramos a la clave
	print algomas['cadenademas']

#ejecutamos la funcion	
funcion(' python ',3,cadenaextra = 'hola john andrey',cadenademas = ' como estas')

def operacion(num1, num2, num3):
	return (num1 + num2) * num3

resultado = operacion(5,5,8)

print "El resultado de la operacion es: "+str(resultado)
