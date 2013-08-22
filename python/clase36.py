#LECTURA DE ARCHIVOS
try:
 	f = open('ejemplo.txt','r')
except:
	exit()
	print "Error de Archivo"
else:
	#f.close()
	print f

print f.read()

#podemos definir cuantos bits queremos leer
print f.read(15)

#toca comentar lo de arribar para poder ejecutarlo
#para leer por lineas usamos readlines
#lineas = f.readlines()
#print lineas