#estructura de control con agenda
#funciones convertir en funciones
def bienvenidos():
	print("Bienvenido al menu de la agenda")
	print("Seleccione una opcion")
	print("1. Insertar o agregar dato a la agenda")
	print("2. Listar los datos de la agenda")
	print("3. Buscar por nombre")

def escribir():
	print("Usted selecciono agregar a la agenda")
	agenda = open("agenda.csv",'a');
	nombre = raw_input("Introduce el nombre de contacto: ")
	telefono = raw_input("Introduce telefono: ")

	print("Se a guardado en la agenda el contacto ",nombre," con numero de telefono ",telefono)

	agenda.write(nombre)
	agenda.write(",")
	agenda.write(telefono)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()

def listar(fin):
	print("Usted selecciono listar datos de la agenda")
	agenda = open("agenda.csv")
	#numero = 0
	#mientras que numero sea menor que 2 ejecute esto
	for i in range(1,fin):
		lectura = agenda.readline()
		print(lectura.replace(",","\t\t"))
		#numero = numero + 1

	print("proceso terminado")
	agenda.close()

def miError():
	print("Esa opcion no existe")

def buscar(nombre):
	print("buscando")
	agenda = open("agenda.csv")
	for i in range(1,30):
		lectura = agenda.readline()
		partido = lectura.split(',')
		if nombre == partido[1]:
			print(partido[2])

	agenda.close()