#Importo mi clase nodo a donde trabajare con mis metodos de la doble lista
from nodo import Nodo
#Creo mi clase lista donde indico que tengo un primer y ultimo dato
class Listade():

	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.tamaño = 0
#Creo mi metodo para ver si mi lista esta vacia o no
	def vacia(self):
		return self.primero == None
#Hago un metodo en el cual podre insertar un dato hasta el final
	def agregar_final(self,dato):
		if self.vacia():
			self.primero =  self.ultimo = Nodo(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.anterior = aux
		self.tamaño += 1
#Hago otro metodo pero esta vez es para poder agregar un dato al inicio
	def agregar_inicio(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero.anterior = aux
			self.primero = aux
		self.tamaño += 1
#Hago mi metodo para eliminar desde el inicio de mi lista
	def eliminar_inicio(self):
		if self.vacia():
			print("La lista esta vacia")
		elif self.primero.siguiente == None:
			self.primero = self.ultimo = None
			self.tamaño = 0
		else:
			self.primero = self.primero.siguiente
			self.primero.anterior = None
			self.tamaño -= 1
#Hago mi metodo para eliminar desde el final de la lista
	def eliminar_final(self):
		if self.vacia():
			print("La lista esta vacia")
		elif self.primero.siguiente == None:
			self.primero = self.ultimo = None
			self.tamaño = 0
		else:
			self.ultimo = self.ultimo.anterior
			self.ultimo.siguiente = None
			self.tamaño -= 1
#Hago mi metodo para imprimir los numeros de derecha a izquierda
	def recorrer_inicio(self):
		aux = self.primero
		while aux:
			print(aux.dato)
			aux = aux.siguiente
#Creo un metodo para imprimir los numeros de izquierda a derecha
	def recorrer_final(self):
		aux = self.ultimo
		while aux:
			print(aux.dato)
			aux = aux.anterior
#Hago un metodo para saber el tamaño de mi lista
	def Tamaño(self):
		return self.tamaño
#Hago un metodo llamado menu que esta fuera de mi clase lista para poder implementar todos mis metodos que hice y desde el menu los mando a llamar		
def Menu(Listade):
	while True:
		print("1.-Agregar los numeros del 1 al 9")
		print("2.-Leer de izquierda a derecha")
		print("3.-leer de derecha a izquiera")
		print("4.-Eliminar el 1 y 8")
		print("5.-Leer la raiz")
		print("6.-Leer final e incio")
		print("7.-Buscar el 0,7,8,1")

		opcion = int(input())

		lista = Listade()

		if opcion == 1:
			print(lista.agregar_final("1"))
			print(lista.agregar_final("2"))
			print(lista.agregar_final("3"))
			print(lista.agregar_final("4"))
			print(lista.agregar_final("5"))
			print(lista.agregar_final("6"))
			print(lista.agregar_final("7"))
			print(lista.agregar_final("8"))
			print(lista.agregar_final("9"))
		elif opcion == 2:
			print("lista.recorrer_inicio()")
			print ("-"*20)
		elif opcion == 3:
			print("lista.recorrer_final()")
			print ("-"*20)
		elif opcion == 4:
			lista.eliminar_inicio()
			print("lista.recorrer_inicio()")
			lista.eliminar_final()
			lista.eliminar_final()
			print("Lista.recorrer_final()")
		elif opcion == 5:
			lista.recorrer_inicio()
		elif opcion == 6:
			lista.recorrer_inicio()
			lista.recorrer_final()
		elif opcion == 7:
			if lista[0] == True:
				print("El valor existe en la lista")
			else:
				print("El valor no existe")
			if lista[7] == True:
				print("El valor  exite en la lista")
			else:
				print("El valor no existe")
			if lista[8] == True:
				print("El valor existe en la lista")
			else:
				print("EL valor no existe")
			if lista[1] == True:
				print("EL valor existe en la lista")
			else:
				print("EL valor no existe")
		else:
			print("Esta opcion no existe")
#Mando a llamar al menu fuera de mis metodos y clases para que se pueda ejecutar correctamente
Menu(Listade)