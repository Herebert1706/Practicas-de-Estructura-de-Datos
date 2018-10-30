#Creo una clas nodo los cuales se iran ligando
class Nodo():
	
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None
		self.anterior = None