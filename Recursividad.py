def naturales(x): //Aqui estoy definiendo una funcion en donde utilizare la variable x
    if x<101:  //Hago un if en donde le doy la condicion que x sea menor que 100
        print(x)  //Mando a imprimir los numeros
        x=x+1  //Aqui incremento el numero de 1 en 1
        return naturales(x) //Regreso la funcion de donde va empezar la suma
print(naturales(1))  //Imprimo los primeros 100 numeros naturales a partir del 1 hasta el 100

