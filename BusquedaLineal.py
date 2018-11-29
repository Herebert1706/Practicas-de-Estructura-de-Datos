#Hago un metodo el cual recibe el nombre del tipo de busque que va a realizar
def BusquedaLineal(lista, elemento):
	i = 0   #Inicio a i como 0 para que al momento de hacer el for pueda ir aunmento o avanzando de 1 en 1
	for z in lista:
		if (z == elemento):    #Ya creado el for donde z esta dentro de la lista y al momento de decir que si z es igual a tal elemento este regresa la i e de igual manera lo aumenta
			return i + 1
		i = i+ 1
	return -1
#Creo mi metodo menu para mandar a llamar mi metodo de busque lineal, dentro de este metodo, creo mi lista y mando a pedir el elemento que se quiere buscar, si existe o no existe
def menu():
	lista = [1,12,33,45,85,78,8,6,55,43,39,91,101,67]
	print(lista)
	print("-"*55)
	print("Escribe un numero de los que estan en la lista :")
	elemento = input(int())
	posicion = BusquedaLineal(lista, elemento)
	if (posicion >- 1):
		print("La posicion del numero es : ", posicion)
	else:
		print("EL elemento no se encuentra en la lista")
#La linea de abajo sirve para que mi metodo menu se pueda ejecutar sin problema alguno y pueda llamar mis metodos
menu()
