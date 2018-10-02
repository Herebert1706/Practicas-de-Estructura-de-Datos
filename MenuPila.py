"""Creo una pila sin valor indice, en donde valor es igual a 0, mi indice tambien es igualado a 0 para asi poder utilizarlos de la mejor manera que me sea mas conveniente"""

Pila = []      
valor = 0
indice = 0

    
def push(valor):            """Defino un metodo push que se refiere a ingresar un dato pero para eso usamos la instruccion append que sirve para agregar elementos """
    Pila.append(valor)          """Al colocar lo escrito en esta linea, estoy diciendo que se agregara un valor a la pila o un elemento nuevo a ella"""
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
	valor = int(input()
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


"""Defino un metodo pop que es conocido para sacar elementos, pero utilizo la instruccion "del" que me sirve para eliminar un elemento, "y en una pila el pop saca al ultimo elemento en entrar a la pila ya que el primerp elemento e entrar a la pila es el ultimo en salir" y le regreso un valor 0 para que se pueda ejecurar"""

def Pop(indice):
	del(pila[indice])   """Aqui indico que voy a eliminar un elemento de la pila"""
	return 0

"""Hago un if para indicar que mientras mi indice sea mayor a 0 puedo seguir eliminando datos de mi pila y cuando ya no tenga ningun dato o valor en mi pila me aparecera null de que ya no hay mas elementos dentro de la pila"""

if indice >= 0:
	print(pila)
	Pop(indice)
	indice -= 1

	print(pila)
	Pop(indice)
	indice -= 1

	print(pila)
	Pop(indice)
	indice -= 1

	print(pila)
	Pop(indice)
	indice -= 1
	
	print(pila)
	Pop(indice)
	indice -= 1

	print(pila)   """Imprimo la pila"""


"""Aqui defino un metodo peek que es para mostrar todos los elementos de la pila, o depende la instruccion que le demos, en mi caso el dato que mandare a imprimir es el ultimo que es el de hasta arriba de la pila"""

def Peek(indice):
	print(pila[indice-1])
	return 0

print("El dato en el tope de la pila es:")      """Imprimo el dato en donde le indico que el indice es igual a mostrar dato de mi mi ultimo indice."""
indice = Peek(indice)


"""Defino un metodo llamado Menu para meter todas las instrucciones o todos los metoso que creamos anteriormente que es el push, pop y peek"""

def Menu():
    while True:
        print("1.- Añadir un elemento a la pila")
        print("2.- Sacar un elemento de la pila")
        print("3.- Imprimir pila")

        opcion = int(input())

        if opcion == 1:
            push()
        elif opcion == 2:
            Pop()
        elif opcion == 3:
            Peek()
        else:
            print("La opcion que usted ingresp no es correcta")

Menu()

