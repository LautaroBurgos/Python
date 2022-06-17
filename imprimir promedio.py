numero1=int(input("Introduzca un numero: "))
numero2=int(input("Introduzca otro numero: "))
numero3=int(input("Introduzca otro numero "))
#
#	PRE:Recibe tres numeros mayores que cero
#	POST:Devuelve el promedio entre los tres
#
def promedio(numero1,numero2,numero3):
	return(((numero1+numero2+numero3)/3))

print("El promedio de los 3 numeros introducidos es: ",promedio(numero1,numero2,numero3))