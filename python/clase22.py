#FUNCION FILTER
def filtro(elem):
	return (elem > 0)

#definimos nuestra lista
l = [1,-3,2,-4,-5,6,7,-8,9]
#usamos la funcion filter y mandamos la funcion filtro y la lista
lr = filter(filtro,l)

print l
print lr

#tambien lo podemos hacer con cadenas
def filtro(elem):
	return (elem == 'o')

s = "hola mundo"
lr = filter(filtro,s)

print s
print lr
