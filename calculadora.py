#	PRE:
#	POST: Devuelve la suma entre dos numeros ingresados por el usuario
def suma():
	print("Escogio suma de 2 numeros")
	num1=solicitar_primer_numero()
	num2=solicitar_segundo_numero()
	return (num1+num2)
#	PRE:
#	POST: Devuelve la resta entre dos numeros ingresados por el usuario
def resta():
	print("Escogio resta de 2 numeros")
	num1=solicitar_primer_numero()
	num2=solicitar_segundo_numero()
	return(num1-num2)
#	PRE:
#	POST: Devuelve la multiplicacion entre dos numeros ingresados por el usuario
def multiplicacion():
	print("Escogio producto de 2 numeros")
	num1=solicitar_primer_numero()
	num2=solicitar_segundo_numero()
	return(num1*num2)
#	PRE:
#	POST: Devuelve la division entre dos numeros ingresados por el usuario
def division():
	print("Escogio division de 2 numeros")
	num1=solicitar_primer_numero()
	num2=solicitar_segundo_numero()
	return(num1/num2)

#
#	POST:Imprime por pantalla el menu para el usuario
def menu():
	print("---------------------")
	print("Calculadora en python")
	print("Que operacion desea realizar?")
	print("1.Suma de 2 numeros")
	print("2.Resta de 2 numeros")
	print("3.Producto de 2 numeros")
	print("4.Division de 2 numeros")
	print("5.Salir")
#	PRE:
#	POST: Devuelve el primer numero de la operacion
def solicitar_primer_numero():
	return float(input("Por favor ingrese el primer numero: "))
#	PRE:
#	POST: Devuelve el segundo numero de la operacion
def solicitar_segundo_numero():
	return float(input("Por favor ingrese el segundo numero: "))

final=False



while(final==False):
	menu()
	operacion=int(input())
	if operacion==1:
		print("El resultado es ",suma())
	elif operacion==2:
		print("El resultado es ",resta())
	elif operacion==3:
		print("El resultado es ",multiplicacion())
	elif operacion==4:
		print("El resultado es ",division())
	else:
		final=True
	