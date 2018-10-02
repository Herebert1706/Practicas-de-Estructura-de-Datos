"""Tengo mi pila hecha como se muestra en la linea de abajo, tambien indico que mi indice tiene un valor de 5, ya que mi pila es de 5 elementos pero como se cuenta desde el 0 por eso se consideran 4 indices"""

pila =[1,2,3,4,5]

i = 4

"""Defino un metodo pop que es conocido para sacar elementos, pero utilizo la instruccion "del" que me sirve para eliminar un elemento, "y en una pila el pop saca al ultimo elemento en entrar a la pila ya que el primerp elemento e entrar a la pila es el ultimo en salir" y le regreso un valor 0 para que se pueda ejecurar"""

def Pop(i):
	del(pila[i])   """Aqui indico que voy a eliminar un elemento de la pila"""
	return 0

"""Hago un if para indicar que mientras mi indice sea mayor a 0 puedo seguir eliminando datos de mi pila y cuando ya no tenga ningun dato o valor en mi pila me aparecera null de que ya no hay mas elementos dentro de la pila"""

if i >= 0:
	print(pila)
	Pop(i)
	i -= 1

	print(pila)
	Pop(i)
	i -= 1

	print(pila)
	Pop(i)
	i -= 1

	print(pila)
	Pop(i)
	i -= 1
	
	print(pila)
	Pop(i)
	i -= 1

	print(pila)   """Imprimo la pila"""




