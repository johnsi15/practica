#EXCEPCIONES EN PYTHON
print "Bienvenido"

try:
	print 'John'
except TypeError:
	print "Error en tipo de dato"
except NameError:
	print "Variable no existe"
except ZeroDivisionError:
	print "No se puede dividir entre 0"
else:
	print "No hubo Error"
finally:
	print "Me ejecuto pase lo que pase"

print "Adios"