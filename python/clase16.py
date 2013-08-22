#METODOS DE PYTHON Y CADENAS....
s = 'Hola Mundo'

#con len podemos contar la cadena
print len(s)

#metodo de count CADENA.count(valor,inicio,fin)
print s.count("o")

print s.count("o",0,3)

#pasar toda la cadena a minusculas
print s.lower()
#con upper pasamos todo a mayuscula
print s.upper()

#metodo replace... cadena.replace(valor,nuevo,repeticiones
print s.replace('o','x')
print s.replace('Hola','Andrey')
print s.replace('o','x',1)

#metodo split cade.split(separador,maxsplit)
print s.split('a')
print s.split('o',1)#asi porque termina en O entonces la limitamos

#metodo find cadena.find(valor,inicio,fin)
print s.find('a')
#con rfind busca de atras para adelante
print s.rfind('o')
#metodo join me devuele la tupla con el ;
t = ("H","o","l","a")
r = ";"
print r.join(t)