#funcion map
def operador(a,b):
	return a+b

l1 = [1,2,3,4]#una lista
t1 = (5,6,7,8)#una tupla

lr = map(operador,l1,t1)

print l1
print t1
print lr

#si hay diferencias entre la lista y la tupla
def operador(a,b):
	if a==None or b==None:
		return 0

	return a+b

l1 = [1,2,3,4]#una lista
t1 = (5,6,7)#una tupla

lr = map(operador,l1,t1)
print l1
print t1
print lr