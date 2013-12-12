
print "Cambios extra rapidos"
opcion = int(input("Que cambio desea realizar Digite 0 - 1 'Cambio de bolivares'"))

if opcion == 0:
	bolivares = float(input("A como esta el bolivar: "))
	pesos = int(input("Valor a cambiar en pesos:"))
	result = pesos/bolivares
	print "Su cambio en bolivares es: %d"%result
else:
	bolivares = float(input("A como esta el bolivar: "))
	bol = int(input("Valor a cambiar en bolivares"))
	result = bolivares*bol
	print "Su cambio en pesos es: %d"%result
