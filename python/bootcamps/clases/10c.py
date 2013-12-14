#importar modulos

import modulos

def principal():
	modulos.bienvenidos()

	opcion = raw_input("> ")

	if opcion == "1":
		modulos.escribir()
		principal()
	elif opcion == "2":
		print("Cuantos registros quieres ver: ")
		cant = raw_input("> ")
		cantidad = int(cant)
		print cantidad
		modulos.listar(cantidad + 1)
		principal()
	elif opcion == "3":
		print("Escriba el nombre")
		nombre = raw_input("> ")
		modulos.buscar(nombre)
		principal()
	else:
		modulos.miError()
		principal()
	#control de flujo
principal()