nombre="Juan"

#PRE:Recibe una cadena de caracteres, o string
#POST:Imprime esta cadena desde el ultimo caracter al primero.
def imprimir_cadena_invertida(cadena):
	largo=len(cadena)
	for i in range(largo):
		print(nombre[largo-1-i]) 

imprimir_cadena_invertida(nombre)