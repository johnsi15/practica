#ENTRADA DE DATOS DESDE EL TECLADO CON rawInput
try:
	valor = raw_input("Tu numero: ")
	valor = int(valor)
except:
	print "Eso no es un numero"
else:
	print "Tu numero es: ",valor