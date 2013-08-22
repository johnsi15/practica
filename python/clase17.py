#encoding: utf-8
#LISTAS Y SUS METODOS....
lista = [1,3,"Dos",3]

buscar = 1
#verificasmoa que exista en la lista con in 
if buscar in lista:
	print lista.index(buscar)#devolvemos el indixe de la lista
else:
	print "NO existe ese elemento"

print lista
#podemos añadir un nuevo elemnto con append
lista.append('nuevo elemento')

print lista

#con count podemos ver cuantas veces esta en la lista
print lista.count(3)
#con insert podemos añadir un nuevo elemento en el index
lista.insert(2,'nuevo')
print lista
#con el metodo estend podemos estender la lista
iterable = (1,2,3,4)
lista.extend(iterable)
print lista
#con el metodo pop podemos sacar un elemto de la lista
print lista.pop(2)
print lista
#con remove podemos borrar la primera ocurencia de la lista
lista.remove(3)
print lista
#con el metodo reverse me da la vuelta a la lista
lista.reverse()