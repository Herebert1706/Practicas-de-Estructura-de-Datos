#Ramirez Herbert Francisco
#Colas dobles o Bicolas
#Push

#Inicializo mi contador en 0
cont = 0
#Creo mi metodo en donde declara mi cola vacia y las variavles que utilizare en los metos siguientes de igual manera imprimo la cola y mando a que me regrese esos valores
def New_cola():
	Cola = [0,0,0,0,0,0,0,0,0,0]

	first_front = 10
	last_front = 10

	first_back = 0
	last_back = 0

	print(Cola)

	return Cola,first_front,last_front,first_back,last_back
#Creo mi metodo para poder agregar un dato desde la parte frontal, para la cual hago unas iteraciones con if para ver si esta vacio y de eso me arroja un mensaje para que agregue el numero que el usuario guste
def Push_front(Cola_,last_front, last_back,cont):
	if Cola_[last_front-1] == 0:
		if last_front == 0:
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_front-1] = item
			last_front = 10
			print(Cola_)
			return Cola_,last_front,cont
		else:
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_front-1] = item
			last_front -= 1
			print(Cola_)
			return Cola_,last_front,cont
#El else que se aplica es para que me diga si la cola ya se encuentra llena que eso es cuando ya se agregaron 10 datos
	else:
		if cont == 10:
			print("Cola llena")
			cont = 0
			return Cola_,last_front,cont
		else:
			if last_front == 0:
				last_front = 10
				return Push_front(Cola_,last_front, last_back,cont)
			else:
				print("-")
				last_front -= 1
				cont += 1
				return Push_front(Cola_,last_front, last_back,cont)
#Declaro mi metodo para agregar datos desde la parte trasera de mi cola, las instrucciones son muy parecidas a la del push frontal entonces este lo que hace se va
#Al ultimo indice de la cola y en ves de avanzar hacia enfrente se va recorriendo hacia atras.
def Push_last(Cola_,last_front,last_back,cont):

	if Cola_[last_back] == 0:
		if last_back == 9:
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_back] = item
			last_back = 0
			print(Cola_)
			return Cola_,last_back,cont
		else:
			print("-" * 25)
			print("Ingresa el numero")
			print("-" * 25)
			item = int(input())
			Cola_[last_back] = item
			last_back +=1
			print(Cola_)
			return Cola_,last_back,cont

	else:
		if cont == 9:
			print("Cola llena")
			cont = 0
			return Cola_,last_back,cont
		else:
			if last_back == 9:
				last_back = 0
				return Push_last(Cola_,last_front, last_back,cont)
			else:
				print("-")
				last_back += 1
				cont += 1
				return Push_last(Cola_,last_front, last_back,cont)

# def Pop_front(Cola_,first_front,first_back,cont):
# 	if Cola_[first_front-1] == 0:
# 		if cont == 10:
# 			print("Cola vacia")
# 			cont = 0
# 			return Cola_,first_front,cont
# 		else:
# 			if first_front == 0:
# 				first_front = 10

# 				return Pop_front(Cola_,first_front,first_back,cont)
# 			else:
# 				first_front -= 1
# 				cont += 1
# 				return Pop_front(Cola_,first_front,first_back,cont)
# 	else:
# 		Cola_[first_front-1] = 0
# 		print(Cola_)
# 		cont = 0
# 		first_front = 10
# 		return Cola_,first_front,cont

# def Pop_last(Cola_,first_front,first_back,cont):
# 	if Cola_[first_back] == 0:
# 		if cont == 10:
# 			print("Cola vacia")
# 			cont = 0
# 			return Cola_,first_back,cont
# 		else:
# 			if first_back == 10:
# 				first_back = 0

# 				return Pop_last(Cola_,first_front,first_back,cont)
# 			else:
# 				first_back += 1
# 				cont += 1
# 				return Pop_last(Cola_,first_front,first_back,cont)
# 	else:
# 		print("Si entro")
# 		Cola_[first_back] = 0
# 		print(Cola_)
# 		cont = 0
# 		first_back = 0
# 		return Cola_,first_back,cont

#Hago mi menu para poder mandar a llamar mis metodos que estuve manejando con mas anterioridad, al momento de escoger una opcion mis metodos se ejecutan para poder realiar la tarea deseada

def Menu(cont):
	while True:
		print("1.-Crear cola")
		print("2.-Anadir un numero al comienzo de la cola")
		print("3.-Anadir un numero al final de la cola")
		# print("4.-Eliminar un dato al comienzo de la cola")
		# print("5.-Eliminar un dato al final de la cola")
		print("0.-Salir")

		Opcion = int(input())

		if Opcion == 1:
			Cola_,first_front,last_front,first_back,last_back = New_cola()

		elif Opcion == 2:
			Cola_,last_front,cont= Push_front(Cola_,last_front,last_back,cont)

		elif Opcion == 3:
			Cola_,last_back,cont = Push_last(Cola_,last_front,last_back,cont)

		# elif Opcion == 4:

		# 	Cola_,first_front,cont = Pop_front(Cola_,first_front,first_back,cont)

		# elif Opcion == 5:

		# 	Cola_,first_back,cont = Pop_last(Cola_,first_front,first_back,cont)

		if Opcion == 0:
			return 0

Menu(cont)
