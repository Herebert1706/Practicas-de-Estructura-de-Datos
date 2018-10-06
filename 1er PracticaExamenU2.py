n=0 #Creo una variable inciandola en 0 para que despues se puede sumar
def numeros(x,n): #Defino un metodo 
    if x <= 9:  #Hago un if donde me dice que x(numeros) tiene que ser menor a o igual a 9, imprimo los numeros y hago una operacion en donde digo que mi numeros es el mismo numeros mas 1 para que asi vaya aunmentando en uno, despues de eso el resultado que es n lo igual a n mas el numero que sigue para que se vayan sumando
        print(x)
        x = x+1
        n = n+x
    else:   #Y aqui como el resultado es como si sumara 10 numeros le reste el ultimo numero y hago una string donde les muestro el resultado, como me generaba un error de desbordamiento hice un ciclo while en donde digo que si ya tengo mi resultado pare con la opcion de break
        print (n-x)
        print ("La suma de los numeros es = ",n-x)
        while (True):
            if n==45:
                break
    return numeros(x,n) #Mando a llamar mi misma funcion para luego imprimir mi funcion
print(numeros(0,0))
