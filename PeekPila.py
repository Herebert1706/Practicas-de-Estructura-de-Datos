"""Creo una pila sin valor indice, en donde valor es igual a 0, mi indice tambien es igualado a 0 para asi poder utilizarlos de la mejor manera que me sea mas conveniente"""

pila = []
item = 0
i = 0

    
def push(item):   """Defino un metodo push que se refiere a ingresar un dato pero para eso usamos la instruccion append que sirve para agregar elementos """      
    pila.append(item)   """Al colocar lo escrito en esta linea, estoy diciendo que se agregara un valor a la pila o un elemento nuevo a ella"""
    return 0      """Regreso un valor cero para que se pueda ejecutar"""  

"""Hago un if en donde le doy la instruccion de que si mi indice es menor a 5 me va a pedir un elemento o valor para agregar a la pila, el vaor puede ser entero o un string, despues se ejecuta el push que es donde guarda el elemento ingresado y por ultimo mi indice va aumentando en uno"""

if i<=5:
	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1

	print("Introduce tu numero")
	item = int(input())
	push(item)
	i = i+1
	print("Pila llena") 

"""Con esta instruccion que es el "else" indico que si quiero agregar mas de 5 elementos, me va a mostrar un mensaje en donde me dira que la pila ya esta llena"""

"""Aqui defino un metodo peek que es para mostrar todos los elementos de la pila, o depende la instruccion que le demos, en mi caso el dato que mandare a imprimir es el ultimo que es el de hasta arriba de la pila"""

def Peek(i):
	print(pila[i-1])
	return 0

print("El dato en el tope de la pila es:")      """Imprimo el dato en donde le indico que el indice es igual a mostrar dato de mi mi ultimo indice."""
i = Peek(i)





