#Creo mi variable valor y mi indice llamado k
valor=0
k=0
#Defino una funcion llamada cola en la cual dentro de ella hago una lista con un indice de 5 en la cual caben 6 valores
def newCola():
    Cola = [0,0,0,0,0,0]
    k=5
    return Cola, k #Regreso el valor de mi cola y de mi indice
##Defino mi funcion encolar en la cual dentro de ella hago un inf diciendo que si mi indice es igual a tal valor me va a pedir que ingrese un valor para la cola
##Hago esto 5 veces mas ya que el indice cuenta desde el 0 hasta el 5
#def Encolar(Cola1,valor,k):
#    if k==5:
#        print("Ingresa el numero que deseas agregar")
#        valor = int(input())
#        Cola1[k] = valor
#        k -= 1
#    elif k==4:
#        print("Ingresa el numero que deseas agregar")
#        valor = int(input())
#        Cola1[k] = valor
#        k -= 1
#    elif k==3:
#        print("Ingresa el numero que deseas agregar")
#        valor = int(input())
#        Cola1[k] = valor
#        k -= 1
#    elif k==2:
#        print("Ingresa el numero que deseas agregar")
#        valor = int(input())
#        Cola1[k] = valor
#        k -= 1
#    elif k==1:
#        print("Ingresa el numero que deseas agregar")
#        valor = int(input())
#        Cola1[k] = valor
#        k -= 1
#    elif k==0:
#        print("Ingresa el numero que deseas agregar")
#        valor = int(input())
#        Cola1[k] = valor
#        k -= 1
#
#    return Cola1, k, valor  #Refreso el valor de Cola1, de mi indice y de mi valor que tiene
##Hago mi funcion desencolar en donde digo que si saco mi indice 5, ahora el siguiente indice que es el 4 se recorrera y asi sucesivamente hasta vaciar la cola
def Desencolar(Cola1,k):
    Cola1[5] = Cola1[4]
    Cola1[4] = Cola1[3]
    Cola1[3] = Cola1[2]
    Cola1[2] = Cola1[1]
    Cola1[1] = Cola1[0]
    Cola1[0] = 0
    k += 1

    return Cola1, k    #Regreso el valor de Cola1 y de mi indice que es el que ando manejando dentro de mi funcion desencolar
##Hago mi funcion para imprimir el dato que tengo en la cola no todos, solo uno que es el ultimo que ingreso a ella
#def Peek(Cola1,valor,k):
#    print(Cola1)
##Hago un menu donde igula utilizare mis variables de valor y mi indice k
def Menu(valor,k):
    while True:    #Creo un ciclo while para darle a elegir las opciones que quiera escoger el usuario.
        print("1.- Crear cola")
#        print("2.- Añadir un elemento a la cola")
        print("3.- Sacar un elemento de la cola")
#        print("4.- Imprimir cola")

        opcion = int(input())       #Creo una variable dentro de esta funcion para utilizarla dentro del if de abajo

        if opcion == 1:     #Si el usuario elige esta opcion se creara una cola
            Cola1,k = newCola()     #Aqui la Cola1  y mi indice los igualo a mi funcion newCola para que se puedan utilizar dentro de todas las funciones que hermos usado ya anteriormente y en esta tambien
#        elif opcion == 2:   #Si el usuario elige la opcion 2 tendra que agregar un valor a la cola y asi repito esto hasta que se llene la cola
#            if k == 5:
#                Cola1,k,valor = Encolar(Cola1,valor,k)
#            elif k == 4:
#                Cola1,k,valor = Encolar(Cola1,valor,k)
#            elif k == 3:
#                Cola1,k,valor = Encolar(Cola1,valor,k)
#            elif k == 2:
#                Cola1,k,valor = Encolar(Cola1,valor,k)
#            elif k == 1:
#                Cola1,k,valor = Encolar(Cola1,valor,k)
#            elif k == 0:
#                Cola1,k,valor = Encolar(Cola1,valor,k)
#            else:       #Si quiero agrgar mas valores de los que se pueden me arrojara el mensaje de la linea de abajo
#                print("LOS ELEMENTOS QUE USTED A INGRESADO HAN LLENADO LA COLA")
        elif opcion == 3:       #Si el usuario escoge esta opcion sacara el primer elemento que fue ingresado a la cola y asi hasta poder vaciarla
            Cola1,k = Desencolar(Cola1,k)
            if k > 5:  #Si mi indice llega a mas de 5 estara vacia ya que se han sacado todos los elementos que se habia agregado
                print("USTED A VACIADO LA COLA")
#        elif opcion == 4:       #Si el usuario escoge la opcion 4 le mostrara el ultimo elemento que hay dentro de la cola con la instruccion peek
#            Peek(Cola1,valor,k)   #Peek me mostraraque en esta tengo mi cola son su valor e indice
            return 0        #Regreso un 0 para que se pueda ejecutar correctamente

Menu(valor,k)       #Mi menu lo pongo aqui para que se pueda ejecutar con todas mis funciones y para que lo pueda utilizar sin ningun problema ya que si lo pongo antes de mi return del menu me generara un error.