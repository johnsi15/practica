#PAQUETES ME VAN A PERMITIR ORDENAR LOS MODULOS
#debemos tener un archivo llamado __init__ para que los reconosca con paquetes
import MM.m
import GM.g

#instancia de la clase#
e = MM.m.Ejemplo()
e.imprime()

#Funcion normal#
MM.m.fEjemplo()

#instancia de la clase#
o = GM.g.Gejemplo()
o.imprime()

#Funcion normal#
GM.g.fEjemplo()