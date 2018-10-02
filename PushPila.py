 """Creo una pila sin valor indice, en donde valor es igual a 0, mi indice tambien es igualado a 0 para asi poder utilizarlos de la mejor manera que me sea mas conveniente"""

Pila = []      
valor = 0
indice = 0

    
def push(valor):            """Defino un metodo push que se refiere a ingresar un dato pero para eso usamos la instruccion append que sirve para agregar elementos """
    pila.append(valor)          """Al colocar lo escrito en esta linea, estoy diciendo que se agregara un valor a la pila o un elemento nuevo a ella"""
    return 0            """Regreso un valor cero para que se pueda ejecutar"""

"""Hago un if en donde le doy la instruccion de que si mi indice es menor a 5 me va a pedir un elemento o valor para agregar a la pila, el vaor puede ser entero o un string, despues se ejecuta el push que es donde guarda el elemento ingresado y por ultimo mi indice va aumentando en uno"""

	print("Introduce tu numero")
	valor = int(input())
	push(valor)
	indice = indice+1

	print("Introduce tu numero")
	valor = int(input())
	push(valor)
	indice = indice+1

	print("Introduce tu numero")
	valor = int(input())
	push(valor)
	indice = indice+1

	print("Introduce tu numero")
	valor = int(input())
	push(valor)
	indice = indice+1

	print("Introduce tu numero")
	valor = int(input())
	push(valor)
	indice = indice+1

"""Con esta ultima instruccion que es el "else" indico que si quiero agregar mas de 5 elementos, me va a mostrar un mensaje en donde me dira que la pila ya esta llena"""

else:
	print("Pila llena")





