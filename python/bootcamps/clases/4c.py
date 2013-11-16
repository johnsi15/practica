#formateado con variables
agenda = open("agenda.csv",'w');

#print(agenda.read())
agenda.truncate()

nombre = raw_input("Introduce el nombre de contacto: ")
telefono = raw_input("Introduce telefono: ")

print("Se a guardado en la agenda el contacto ",nombre," con numero de telefono ",telefono)

agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write(",")
agenda.write("\n")