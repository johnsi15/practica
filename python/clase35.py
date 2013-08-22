#ESCRITURA DE ARCHIVOS
try:
 	f = open('ejemplo.txt','w')
except:
	exit()
	print "Error de Archivo"
else:
	#f.close()
	print f

f.write("Hola Estoy creando mi primer ")

f.seek(11)#con seek movemos el puntero 

f.write(' intruso')

agregar = ["Hola Mundo\n","\tProgramando ando..."]

f.writelines(agregar)#con writelines podemos agregar listas o tuplas

f.close()