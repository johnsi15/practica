#CON LOS MODULOS PODEMOS ORDENAR EL CODIGO....
#tener en cuenta si queremos importar todo con la otra forma 
#porque de esta forma podemos especificar que modulo es el que quiero 
#para no tener problemas de funciones de = nombre en distintos modulos ok
import clase32m#cargamos el modulo de esta manera

#print clase32m
e = clase32m.Ejemplo()#instanciamos el objeto de la clase Ejemplo atraves del modulo clase32m

e.imprime()#usamos el metodo imprime con el objeto e

clase32m.fEjemplo()

print 'otra forma de importar'
#tambien lo podemos hacer de esta manera
from clase32m import *
e = Ejemplo()
e.imprime()

fEjemplo()