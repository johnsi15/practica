
print "Welcome of Python Andrey"
sueldo = int(input("Digite el sueldo por favor?"))
#sueldo = raw_input("Digite el sueldo por favor? ")

if sueldo < 1000:
	aumento = (sueldo*15)/100
	nvsueldo = sueldo+aumento
	print "Su nuevo sueldo es de: %d"%nvsueldo
else:
	print "El sueldo es mayor a lo estimulado "
