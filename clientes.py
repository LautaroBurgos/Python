clientes=["Jose","Guillermo","Mariano"]
final=False
#
#	PRE: accion debe ser un numero entre 1 y 3
#	POST: ejecuta una de las 3 acciones posibles
#
def ejecutar_accion(accion):
	if accion==1:
		print (clientes)
	if accion==2:
		nuevo_cliente=str(input("Introduzca el nombre del cliente a agregar: "))
		clientes.append(nuevo_cliente)
	if accion==3:
		clientes.remove(str(input("Introduzca el nombre del cliente a ser borrado: ")))



while(final==False):
	print("Sistema de guardado de clientes")
	print("Que accion desea realizar?")
	print("1. Leer  lista de clientes")
	print("2. Agregar un cliente nuevo")
	print("3. Borrar un cliente de la lista")
	print("4. Salir")
	accion=int(input())

	if(accion<4 and accion>0):
		ejecutar_accion(accion)
	elif (accion==4):
		final=True
	else:
		print("El valor introducido no es valido, Introduzca un valor entre 1 y 4")



