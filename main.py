#Importo mi lista para poder imprimir los numeros
from listadobleenlazada import Listade
#Creo una variable que es referente a mi clase lista
lista = Listade()
#Comienzo agregar los datos que se me piden y los imprimo, tambien los borro y vuelo a imprimir para despues mostrarlos de nuevo
lista.agregar_final(1)
lista.agregar_final(2)
lista.agregar_final(3)
lista.agregar_final(4)
lista.agregar_final(5)
lista.agregar_final(6)
lista.agregar_final(7)
lista.agregar_final(8)
lista.agregar_final(9)
lista.recorrer_inicio()
print ("-"*20)
lista.recorrer_final()
print ("-"*20)
lista.eliminar_final()
lista.eliminar_final()
lista.agregar_final(9)
lista.agregar_final(10)
lista.agregar_final(11)
lista.agregar_final(13)
lista.eliminar_inicio()
lista.recorrer_inicio()
print ("-"*20)
lista.recorrer_final()
print-("-"*20)
