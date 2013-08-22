#DICCIONARIOS Y SUS METODOS.....
diccionario = {
	"redes_sociales":['Twitter','Facebook','Badoo'],
	3: 'Tres',
	'Hola': "Mundo"
}

#con el metodo has_key verificamos si en nuestro dicionario existe una clave
print diccionario.has_key(4)
#con el metodo items nos devuelve una tuplas y listas
print diccionario.items()
#con el metodo keys me devuelve una lista unicamente con las claves
print diccionario.keys()
#con el metodo values me devuelve son los valores de la lista
print diccionario.values()
#con el metodo pop eliminamos la clave diccionario.pop(valor,d)
print diccionario
print diccionario.pop(3)
#si no existe la clave podemos darle un valor para que no nos de error
print diccionario.pop(4,-1)
print diccionario
#con del podemos eliminar unicamente a clave
print diccionario
del diccionario['Hola']
#con clear podemos eliminar todos lo elementos del diccionario
diccionario.clear()
#de esta manera modemos agregar un nuevo elemento al diccionario
diccionario["clave nueva"] = 'valor'
print diccionario
#con el metodo copy podemos copiar el diccionario
diccionario_2 = diccionario.copy()
print diccionario
print diccionario_2
