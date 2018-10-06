cliente=0   #Hago mi varial¡ble cliente de 0 y el lugar que es igual al indice lo coloco en 0 tambien.
lugar=0
def newCola():      #Creo mi metodo cola donde dentro de ella hago la cola que sera llenada con 5 elementos y es decir 4 lugares ya que se cuenta desde el 0 y regreso los valores de mi Cola y el lugar
    Cola = [0,0,0,0,0]
    lugar=4
    return Cola, lugar

def Encolar(Cola1,cliente,lugar):       #Hago otro metodo llamada encolar que es el push en donde le digo que si el lugar es igual a tal, voy agregar el valor que le coloque y asi repetidamente 5 veces
    if lugar == 4:
        print("Ingresa el numero que deseas agregar")
        cliente = int(input())
        Cola1[lugar] = cliente
        lugar -= 1
    elif lugar == 3:
        print("Ingresa el numero que deseas agregar")
        cliente = int(input())
        Cola1[lugar] = cliente
        lugar -= 1
    elif lugar == 3:
        print("Ingresa el numero que deseas agregar")
        cliente = int(input())
        Cola1[lugar] = cliente
        lugar -= 1
    elif lugar == 2:
        print("Ingresa el numero que deseas agregar")
        cliente = int(input())
        Cola1[lugar] = cliente
        lugar -= 1
    elif lugar == 1:
        print("Ingresa el numero que deseas agregar")
        cliente = int(input())
        Cola1[lugar] = cliente
        lugar -= 1
    elif lugar == 0:
        print("Ingresa el numero que deseas agregar")
        cliente = int(input())
        Cola1[lugar] = cliente
        lugar -= 1

    return Cola1, lugar, cliente

def Desencolar(Cola1,lugar):        #Aqui hago mi metodo pop que es Desencolar, donde si saco mi primer valor el sig de la cola tomara esa posicion y asi para mis 5 elementos
    
    Cola1[4] = Cola1[3]
    Cola1[3] = Cola1[2]
    Cola1[2] = Cola1[1]
    Cola1[1] = Cola1[0]
    Cola1[0] = 0
    lugar += 1

    return Cola1, lugar

def Peek(Cola1,cliente,lugar):      #Muestro el elemento de la cola
    print(Cola1)

def Menu(cliente,lugar):        #Creo un menu en el cual desde el podre aplicar los metodos anteriormente creados, hago 4 opciones, creo mi variable opcion para poder usarla, por cierto para hacer el menu uso un ciclo while.
    while True:
        print("1.- Crear cola")
        print("2.- Añadir un NoCliente a la cola")
        print("3.- Sacar un cliente de la cola")
        print("4.- Imprimir cola")

        opcion = int(input())

        if opcion == 1:     #Indico que si el usuario presiona la opcion 1 se crea una cola que esta vacia con 5 espacios.
            Cola1,lugar = newCola()
        elif opcion == 2: #Si el usuario ingresa la opcion 2 puede agregar un cliente a la cola y asi lo hago 4 veces mas para llenar los 5 espacios.
            if lugar == 4:
                Cola1,lugar,cliente = Encolar(Cola1,cliente,lugar)
            elif lugar == 3:
                Cola1,lugar,cliente = Encolar(Cola1,cliente,lugar)
            elif lugar == 2:
                Cola1,lugar,cliente = Encolar(Cola1,cliente,lugar)
            elif lugar == 1:
                Cola1,lugar,cliente = Encolar(Cola1,cliente,lugar)
            elif lugar == 0:
                Cola1,lugar,cliente = Encolar(Cola1,cliente,lugar)
            else:       #Si quiere agregar mas cliente no lo dejara ya que ha llenado todos los lugares de la cola
                print("LOS CLIENTES QUE SE FORMARON HAN LLENADO LA COLA")
        elif opcion == 3:       #Si el usuario presiona 3 se aplicara el metodo pop donde sacara el primer elemento que fue ingresado a la cola
            Cola1,lugar = Desencolar(Cola1,lugar)
            if lugar > 4:
                print("LA COLA A QUEDADO VACIA")
        elif opcion == 4:       #Si el usuario presiona la opcion 4 te muetra el ultimo valor que tienes en la cola
            Peek(Cola1,cliente,lugar)
            return 0

Menu(cliente,lugar)         #Mando llamar mi metodo menu para que lo ejecute con mis variables principales
