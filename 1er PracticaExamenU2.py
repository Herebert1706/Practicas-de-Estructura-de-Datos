def numeros(x,n):   #Creo mi funcion llamado numeros en los cuales utilizare la x y n dentro de el
    if x < 10:      #Si la x es menor 10, entonces se iran sumando de uno en uno los numeros y escribiendo consecutivamente hasta el 9
        n = n +x
        x += 1
        return numeros(x,n)     #Mando a llamar mi funcion con los parametros
    print ("La suma de los numeros es ", n)     #Imprimo el resultado de la suma de los primero 9 numeros

numeros(1,0)        #Pongo mi funcion y le digo que empezara desde el 1 esto es necerario para que pueda ejecutarse el programa.
    
