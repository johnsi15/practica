#encoding: utf-8
#Sentencias Condicionales
edad = 17
m_edad = 18 

"""
if edad >= m_edad:
	print "Eres mayor de edad"
else:
	print "No eres mayor de edad..."

"""

if edad >= 0 and edad < 18:
	print "Eres un niño"
elif edad >= 18 and edad < 27:
	print "Eres un joven"
elif edad >= 27 and edad < 60:
	print "Eres un adulto"
else:
	print "Eres de la tercera edad"