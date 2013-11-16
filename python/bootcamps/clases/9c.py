#estructura de control con agenda
print("Bienvenido al menu de la agenda")
print("Seleccione una opcion")
print("1. Insertar o agregar dato a la agenda")
print("2. Listar los datos de la agenda")

opcion = raw_input("> ")

if opcion == "1":
	print("Usted selecciono agregar a la agenda")
elif opcion == "2":
	print("Usted selecciono listar datos de la agenda")
else:
	print("Esa opcion no existe")
#control de flujo