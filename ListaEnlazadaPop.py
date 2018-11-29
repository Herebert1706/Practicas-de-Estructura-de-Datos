#Listas enlazadas
i = 0
#Creo una clase nodo en la cual con este se podran agregar datos a ca espacio de la lista
class Nodo(object):

	def __init__(self,data):
		self.data = data
		self.next = None

	# def get_data(self):
	# 	return self.data
#Hago mi metodo push en e cual si i es menor que 5 sera iran cumpliendo las condiciones de que si q esta vacion entonces 
#Agregara dato y ya para que agregue el siguiente numero se pregunta que si en la posicion 1 hay un elemento entonces dira que si y avanzara al siguiente campo
#Y asi haciendo esto 5 veces hasta llenar todo
def push(q,i,p):

	if i < 5:
		if q.next != None:

			print("Ingresa el dato")
			data = input()
			p = Nodo(data)
			q.next = p
			q = p
			i += 1

			return q,p,i

		else:

			print("Ingresa el dato")
			data = input()	
			p = Nodo(data)
			q.next = p
			q = p
			i += 1

			return q,p,i

	else:
		print("Lista llena")

		return menu(r,q,i,p)
#Hago mi metodo para ver todos los elementos que hay dentro de la lista
def peek_all(r,q,i):
	cont_local = 0
	q = r
	while cont_local < i+1:
		print(q.data)
		if q.next != None:
 			q = q.next
 		else:
 			return 0
#Creo un metodo para ver un elemento que es el que esta a lo ultimo de la lista
def peek_last(r,q,p):
	print(p.data)
 	return 0
#Creo otro metodo para ver el primer elemento que hay dentro de mi lista
def peek_first(r,q):
 	print(r.next.data)
 	return 0
#Creo este metodo para saber si hay un elemento dentro de la lista
def peek_if(r,q,i):
 	cont_local = 0
 	q = r

 	comp = input("Ingresa el dato a comprobar")
 	while cont_local < i+1:

 		if q.next != None:
 			if comp == q.data:
 				print("El dato esta en la lista")
 				return 0
 			else:
				print("-"*25)
 				q = q.next
 		else:

 			return 0
#Hago un metodo el cual me va a servir para eliminar algun dato que este dentro de la lista, al momento de esto lo que se hace es que
#Se comprueba si el numero esta dentro de ella y si existe se puede eliminar siempre y cuando sea un numero que no sea la raiz
#Ya que si se eliminar la raiz se pierde el enlace
def pop(r,q,i,p):
	cont_local = 0
 	q = r.next
 	helpy_last = r
 	helpy_front = q.next
 	#Aqui declaro una variable la cual me va a servir para pedir el elemento que se desee eliminar
 	comp = input("Ingresa el dato a eliminar --->")
 	#Un cilo while en donde mi contador local sea menor que el indice i+1
 	while cont_local < i+1:
 		#El if incial sirve para que al momento de que pida que elemento desea eliminar, y de pura casualidad elija la raiz para eliminar, este le dara un mensaje de que no se puede eliminar
 		if q.next != None:
 			if comp == r.data:
 				print("No se puede eliminar la Raiz")
 				return 0
#Si no elige la raiz para eliminar lo que hara es comprobar si el elemento existe dentro de la lista lo va a eliminar y el elemento que esta enfrente se va a recorrer un espacio atras
 			else:
 				if comp == q.data and comp != r.next.data:
 					helpy_last.next = helpy_front
 					q.next = None
 					i -=1
 					return i
#Si esto se cumple el dato sera eliminado
 				elif comp == r.next.data:
 					r.next = helpy_front
 					i -=1
 					print("Dato eliminado")

 					return i

 				else:

 					print("-"*25)
 					helpy_last = helpy_last.next
 					q = helpy_last.next
 					helpy_front = q.next
 		else: #Este else es para que al momento de aplicar todo lo anterior me diga que si se elimino el dato y si no exite  ese dato pues no podra ser eliminado
 			if q.next == None and comp == q.data:
 				helpy_last.next = None
 				q = r
 				i -=1
 				print("Dato eliminado")
 				return i
 			else:
 				print("El dato no esta en la lista")
 			return 0

inicio

r = Nodo("Raiz")
q = r
p = r

#Hago un menu en el cual mando a llamar a mis metodos, para que se puedan pedir los numeros, verlos, etc.
def  menu(r,q,i,p):
	while True:

		print("1.-Agregar un dato")
		print("2.-Imprimir la lista")
	    print("3.-Imprimir el ultimo dato agregado")
		print("4.-Imprimir el primer dato agregado")
	    print("5.-Comprobar si hay un dato en la lista")
		# print("6.-Eliminar un dato")
		print("0.-Salir del programa")

		opcion = int(input())

		if opcion == 1:

			q,p,i = push(q,i,p)

		if opcion == 2:
			peek_all(r,q,i)


		if opcion == 3:
			peek_last(r,q,p)


		if opcion == 4:
			peek_first(r,q)


		if opcion == 5:
			peek_if(r,q,i)


		if opcion == 6:
			i = pop(r,q,i,p)



		if opcion == 0:

			print("Adios")
			return 0

menu(r,q,i,p)