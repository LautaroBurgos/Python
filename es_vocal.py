# PRE:	recibe un caracter valido
# POST:	Devuelve true si el caracter es una vocal mayuscula o false en caso contrario
def es_vocal_mayuscula(letra):
	if ((letra=='A') or  (letra=='E') or (letra =='I') or(letra=='O')  or (letra=='U')):
		return True
	else:
		return False

# PRE:	recibe un caracter valido
# POST:	Devuelve true si el caracter es una vocal minuscula o false en caso contrario
def es_vocal_minuscula(letra):
	if ((letra=='a') or  (letra=='e') or (letra =='i') or(letra=='o')  or (letra=='u')):
		return True
	else:
		return False

letra=str(input("Ingrese una letra: "))
if (es_vocal_mayuscula(letra) or es_vocal_minuscula(letra) ):
	print ("La letra ingresada es una vocal.")
else:
	print("La letra ingresada es una consonante.")