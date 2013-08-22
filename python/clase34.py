 #encoding: utf-8
 #ARCHIVOS EN PYTHON
 #r: Solo lectura. El archivo debe existir
 #W: Escritura. si el archivo no existe crea uno nuevo, si existe, lo sobreescribe
 #a: Añadir. Añade el contenido al final del archivo ya existe
 #r+: Lectura y escritura. El archivo debe existir
try:
 	f = open('ejemplo.txt','r+')
except:
	print "Error de Archivo"
else:
	f.close()
	print f
