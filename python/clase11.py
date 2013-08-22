edad = 0
#Bucle while
while edad <= 20:
	if edad == 15:
		edad = edad + 1
		#break
		#continue

	print "Tienes: "+ str(edad)
	#print edad
	edad = edad + 1

lista = ['Elemento 1','Elemento 2','Elemento 3']
#todo lo que este en las lista queda en cosa
for cosa in lista:
    print cosa

#podemos recorer cadenas
for letra in 'cadenas':
	print letra

tupla = 1,2,3,"john"

for num in tupla:
	print num