#FUNCION LAMBDA
li = [1,-2,1,-4]
lo = [5,3,6,7]
s = "Hoola Mundo"
#con lambda no necesitamos definer funciones para realizar las operaciones
suma = lambda n,m: n+m

print map(suma,li,lo)
print filter(lambda n: n=='o',s)
print reduce(suma,lo)

print suma(3,5)