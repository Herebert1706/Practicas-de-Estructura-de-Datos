print("Ingrese a que potencia desea elevar el numero 2")    #Pido el numero que el usuario quiera para eleverar el 2
Potencia = int(input())     #Hago mi variable Potencia a la cual le daremos el valor que quiera el usuario
NumDef=2    #El numero que ya tenemos por default
def exponente(Potencia, NumDef):    #Defino un metodo llamado exponente donde dentro de el hago un if diciendo que si la potencia es mayor a 0 la operacion va aser realizada, dentro del if hago el ciclo while para hacer la operacion el numero 2 que ya teniamos es igual a 2 por 2y luego la instruccion de Potencia es igual a Potencia menos uno para que genere bien la operacion y resultado.
    if Potencia > 0:
        while Potencia >1:
            NumDef = NumDef*2
            Potencia -= 1
            return exponente(Potencia, NumDef)      #Mando a llamar mi meto que defini por las varibles utilizadas dentro de este
        print ("El resultado de 2 elevado al exponente que usted ingreso es = ",NumDef)     #Imprimo el resultado
exponente(Potencia,NumDef)      #Indicp que la funcion exponente lleva dentro los valores del numero por default y la potencia que se utilizara


