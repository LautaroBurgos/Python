#	PRE: 
#	POST: El parametro cadena se repite la cantidad de veces que recibe, separado solo por
#			un espacio.
def imprimir_n_veces(cadena,veces):
	i=0
	for i in range (veces):
		print(cadena ,end=" ")

cadena=(input("Ingrese una letra, palabra o frase: "))
veces=int(input("Ingrese la cantidad de veces que quiera que se repita: "))
imprimir_n_veces(cadena,veces)