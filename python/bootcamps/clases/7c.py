#promediado
suma = 0 
for i in range(0,2):
	nombre = raw_input("Nombre Numero %d "%i)
	edad = raw_input("Edad Numero %d "%i)
	suma = int(suma) + int(edad) 

promedio = suma/2

print("EL promedio de las edades es ",promedio)