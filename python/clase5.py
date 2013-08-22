#Comillas simples - \n es para salto de linea
cad = 'texto entre \n comillas simples'

#Comillas dobles \t es para tabular 
cad2 = "texto en \n\tcomillas dobles"

#Comillas triples
cad3 = """ HOla soy texto 
nuevo como vamos
:)
"""
print type(cad)
print cad2
print cad3

#Repaticion y concatenacion
cad = "texto " * 3
tex1 = "Hola "
tex2 = "Como estas"

print cad
print tex1+tex2

#Datos Booleanos y Operadores Logicos
bt = True
bf = False

bAnd = True and False
bOr = True or False
bNot = not True

print bAnd
print bOr
print bNot