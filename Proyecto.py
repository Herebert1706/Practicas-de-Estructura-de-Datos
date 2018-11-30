#Importo los metodos para poder usar el tiempo en operaciones en el programa
from datetime import datetime, date, time, timedelta
#Proyecto final donde estan estan juntos los metodos de ordenamientos
#defino mi metodo en donde i esta igualado a un numero y en cada numero diferente hay un array difente que lo saque de un programa que hice para realizar numeros aleatorios
#Cada que ponga un arreglo me va a regresar el mismo arreglo para que no genere ningun error
def Arreglos(i):
	if i == 1:
		array = [36, 26, 7, 21, 39, 29, 20, 15, 4, 20, 44, 42, 39, 41, 32, 35, 10, 23, 22, 5, 37, 17, 46, 1, 50, 4, 29, 27, 44, 15, 14, 50, 42, 32, 2, 17, 49, 18, 28, 7, 47, 13, 45, 9, 47, 25, 34, 35, 39, 21]
		return array
	elif i == 2:
		array = [30, 17, 49, 3, 12, 32, 47, 16, 47, 42, 41, 3, 38, 18, 27, 42, 44, 29, 2, 14, 6, 23, 28, 15, 20, 37, 29, 22, 18, 25, 46, 12, 29, 45, 7, 44, 23, 24, 7, 39, 5, 10, 43, 1, 24, 4, 40, 14, 41, 6]
		return array
	elif i == 3:
		array = [39, 7, 42, 46, 44, 2, 50, 38, 41, 21, 19, 17, 33, 49, 33, 11, 43, 7, 12, 30, 21, 48, 49, 32, 37, 15, 41, 28, 50, 19, 2, 48, 2, 26, 44, 40, 7, 39, 43, 22, 49, 21, 24, 6, 5, 24, 3, 10, 45, 15]
		return array
	elif i == 4:
		array = [28, 26, 23, 41, 6, 24, 16, 30, 23, 12, 10, 20, 39, 9, 15, 6, 12, 40, 20, 29, 29, 44, 1, 32, 22, 43, 32, 6, 26, 19, 4, 2, 4, 43, 21, 2, 50, 12, 6, 13, 37, 32, 9, 50, 46, 6, 3, 12, 8, 35]
		return array
	elif i == 5:
		array = [17, 4, 45, 9, 22, 23, 14, 33, 5, 6, 4, 34, 8, 39, 33, 16, 22, 0, 39, 43, 7, 14, 10, 18, 46, 30, 31, 28, 40, 33, 28, 19, 9, 1, 38, 26, 9, 30, 35, 14, 35, 49, 2, 49, 20, 29, 45, 3, 30, 39]
		return array
	elif i == 6:
		array = [8, 12, 20, 21, 41, 34, 15, 46, 14, 32, 46, 27, 24, 13, 47, 6, 8, 3, 18, 38, 9, 26, 49, 1, 31, 22, 33, 33, 0, 31, 12, 17, 23, 2, 44, 14, 47, 27, 18, 41, 0, 0, 30, 28, 26, 50, 2, 8, 32, 32]
		return array
	elif i == 7:
		array = [42, 2, 49, 23, 5, 23, 19, 21, 10, 25, 42, 47, 37, 6, 31, 2, 21, 48, 17, 1, 48, 1, 30, 4, 18, 19, 36, 29, 45, 33, 27, 43, 0, 8, 4, 25, 24, 49, 24, 2, 16, 42, 46, 16, 24, 23, 10, 5, 28, 30]
		return array
	elif i == 8:
		array = [23, 22, 40, 44, 30, 8, 24, 46, 46, 14, 9, 39, 40, 38, 38, 8, 50, 27, 10, 30, 50, 39, 45, 49, 24, 39, 1, 2, 4, 28, 50, 24, 18, 14, 18, 36, 36, 32, 16, 8, 5, 2, 21, 16, 45, 50, 25, 19, 10, 34]
		return array
	elif i == 9:
		array = [50, 22, 42, 41, 2, 32, 30, 2, 5, 27, 40, 39, 22, 21, 1, 24, 4, 1, 47, 33, 31, 44, 22, 15, 28, 22, 22, 20, 38, 13, 37, 4, 40, 10, 43, 46, 36, 26, 21, 3, 30, 28, 37, 42, 22, 12, 17, 30, 27, 12]
		return array
	elif i == 10:
		array = [22, 31, 24, 8, 1, 43, 34, 40, 45, 45, 14, 21, 6, 4, 33, 7, 49, 29, 5, 1, 2, 30, 41, 39, 38, 49, 30, 4, 20, 12, 40, 12, 39, 39, 14, 27, 16, 35, 36, 42, 8, 48, 39, 16, 37, 34, 50, 36, 39, 2]
		return array
	elif i == 11:
		array = [6, 22, 15, 17, 27, 46, 31, 50, 15, 0, 32, 42, 5, 3, 8, 30, 50, 45, 14, 8, 50, 47, 9, 5, 4, 48, 17, 18, 18, 41, 36, 14, 11, 15, 41, 13, 29, 27, 34, 33, 9, 26, 32, 26, 8, 31, 25, 46, 40, 10]
		return array
	elif i == 12:
		array =  [21, 7, 30, 26, 17, 14, 30, 46, 13, 49, 14, 34, 47, 48, 41, 2, 5, 47, 7, 14, 42, 0, 11, 15, 4, 35, 41, 39, 18, 49, 22, 10, 27, 40, 26, 42, 42, 37, 39, 2, 35, 12, 42, 3, 14, 18, 47, 49, 1, 23]
		return array
	elif i == 13:
		array = [25, 5, 12, 1, 49, 34, 1, 30, 13, 13, 19, 7, 21, 5, 46, 43, 11, 47, 36, 43, 18, 34, 26, 23, 12, 12, 9, 9, 25, 27, 41, 33, 8, 27, 12, 43, 43, 40, 17, 50, 10, 11, 0, 4, 4, 30, 8, 16, 17, 4]
		return array
	elif i == 14:
		array = [0, 49, 39, 21, 13, 35, 15, 32, 12, 25, 48, 45, 0, 27, 48, 0, 13, 1, 0, 34, 7, 45, 15, 22, 36, 6, 27, 14, 39, 50, 7, 10, 8, 43, 49, 28, 34, 23, 45, 34, 14, 21, 33, 42, 41, 29, 36, 32, 10, 39]
		return array
	elif i == 15:
		array = [7, 22, 11, 40, 34, 34, 16, 44, 38, 45, 30, 41, 26, 25, 2, 14, 14, 26, 12, 45, 45, 16, 9, 26, 0, 9, 37, 37, 36, 24, 11, 21, 41, 1, 28, 49, 8, 19, 3, 29, 33, 33, 35, 32, 41, 31, 0, 21, 8, 7]
		return array
	elif i == 16:
		array = [18, 42, 16, 28, 25, 23, 37, 7, 28, 48, 26, 47, 6, 35, 41, 23, 16, 24, 13, 4, 22, 19, 46, 15, 11, 7, 41, 41, 6, 39, 25, 22, 50, 42, 26, 23, 3, 29, 13, 45, 11, 25, 18, 36, 49, 18, 11, 34, 46, 43]
		return array
	elif i == 17:
		array = [29, 23, 34, 18, 26, 25, 18, 48, 11, 20, 50, 11, 1, 35, 41, 41, 25, 15, 27, 44, 3, 12, 45, 46, 35, 10, 2, 37, 2, 44, 29, 0, 20, 12, 50, 34, 25, 31, 29, 39, 2, 3, 35, 45, 18, 48, 10, 15, 32, 37]
		return array
	elif i == 18:
		array = [48, 17, 40, 39, 3, 11, 4, 24, 47, 15, 22, 29, 10, 29, 45, 10, 33, 12, 28, 33, 36, 38, 43, 38, 18, 22, 5, 43, 15, 13, 16, 12, 41, 5, 21, 18, 7, 28, 7, 49, 28, 45, 21, 44, 11, 13, 15, 1, 39, 22]
		return array
	elif i == 19:
		array = [13, 11, 35, 49, 22, 4, 44, 23, 23, 49, 41, 47, 36, 25, 10, 48, 24, 44, 36, 28, 50, 28, 3, 50, 12, 36, 45, 16, 17, 18, 46, 25, 25, 32, 33, 29, 50, 16, 37, 25, 23, 9, 2, 19, 27, 30, 36, 43, 19, 46]
		return array
	elif i == 20:
		array = [12, 3, 22, 4, 27, 17, 2, 42, 27, 4, 42, 28, 28, 28, 45, 22, 28, 46, 40, 50, 1, 12, 26, 24, 33, 16, 24, 22, 36, 25, 1, 19, 2, 22, 34, 43, 13, 30, 15, 12, 42, 26, 49, 31, 49, 9, 32, 47, 40, 35]
		return array
	elif i == 21:
		array = [31, 32, 6, 12, 38, 22, 48, 13, 17, 11, 32, 5, 8, 3, 36, 24, 41, 3, 5, 29, 3, 25, 9, 5, 21, 9, 28, 29, 36, 20, 33, 32, 36, 26, 6, 22, 1, 47, 1, 16, 7, 1, 13, 8, 43, 26, 48, 46, 25, 11]
		return array
	elif i == 22:
		array = [39, 27, 20, 22, 2, 1, 18, 9, 21, 28, 30, 9, 48, 16, 19, 42, 39, 44, 3, 42, 48, 3, 29, 29, 33, 8, 7, 20, 44, 6, 23, 11, 1, 30, 29, 9, 28, 28, 10, 3, 33, 23, 7, 37, 11, 43, 9, 50, 30, 40]
		return array
	elif i == 23:
		array = [17, 34, 42, 14, 22, 40, 20, 11, 18, 0, 11, 29, 23, 14, 35, 1, 50, 31, 42, 50, 11, 27, 16, 50, 0, 4, 49, 21, 31, 21, 34, 29, 17, 30, 39, 31, 41, 33, 45, 33, 2, 42, 10, 48, 24, 1, 0, 7, 13, 7]
		return array
	elif i == 24:
		array = [23, 38, 25, 18, 30, 36, 17, 13, 25, 19, 24, 39, 13, 1, 38, 23, 24, 1, 12, 22, 28, 7, 34, 34, 41, 15, 24, 9, 36, 7, 7, 3, 21, 31, 39, 21, 11, 31, 17, 42, 48, 15, 22, 6, 27, 28, 26, 30, 0, 15]
		return array
	elif i == 25:
		array = [21, 45, 37, 31, 4, 30, 6, 2, 32, 48, 34, 7, 38, 24, 18, 18, 30, 49, 2, 41, 20, 29, 9, 39, 13, 30, 19, 26, 23, 27, 7, 41, 32, 14, 23, 42, 5, 8, 41, 33, 10, 15, 36, 17, 0, 14, 42, 45, 19, 11]
		return array
	elif i == 26:
		array = [23, 46, 25, 12, 9, 8, 36, 35, 9, 17, 17, 26, 45, 49, 39, 12, 12, 2, 0, 24, 41, 34, 16, 19, 50, 4, 12, 8, 45, 44, 23, 28, 23, 20, 17, 4, 4, 16, 7, 0, 44, 33, 42, 36, 5, 9, 37, 14, 0, 20]
		return array
	elif i == 27:
		array = [1, 1, 35, 44, 30, 19, 6, 15, 45, 16, 30, 38, 15, 33, 45, 43, 8, 16, 34, 48, 50, 26, 41, 40, 8, 48, 50, 23, 39, 21, 20, 27, 20, 50, 41, 30, 21, 45, 14, 46, 40, 18, 36, 29, 8, 0, 6, 42, 6, 21]
		return array
	elif i == 28:
		array = [21, 2, 43, 34, 22, 23, 50, 15, 49, 8, 39, 45, 29, 9, 46, 11, 25, 50, 47, 34, 6, 14, 0, 43, 5, 43, 2, 22, 38, 36, 18, 44, 9, 30, 17, 31, 31, 42, 46, 23, 31, 31, 46, 12, 7, 40, 27, 25, 42, 15]
		return array
	elif i == 29:
		array = [1, 2, 32, 26, 5, 40, 23, 13, 21, 28, 27, 17, 41, 47, 12, 11, 34, 47, 31, 40, 16, 13, 22, 22, 21, 2, 16, 9, 2, 29, 50, 42, 44, 29, 40, 13, 28, 45, 47, 24, 41, 23, 19, 46, 28, 35, 32, 38, 5, 43]
		return array
	elif i == 30:
		array = [19, 50, 37, 9, 15, 6, 45, 8, 5, 47, 37, 38, 9, 11, 21, 41, 49, 43, 47, 46, 25, 38, 50, 43, 22, 43, 47, 44, 22, 1, 47, 10, 40, 37, 19, 0, 32, 39, 22, 18, 34, 44, 34, 14, 13, 37, 35, 24, 18, 40]
		return array
	elif i == 31:
		array = [38, 47, 47, 11, 46, 5, 22, 20, 17, 32, 13, 0, 33, 29, 41, 2, 49, 25, 28, 3, 46, 46, 38, 49, 5, 18, 41, 11, 1, 21, 6, 24, 43, 20, 21, 45, 15, 9, 37, 27, 46, 45, 35, 28, 1, 2, 44, 12, 21, 7]
		return array

#de la linea 102 hasta la 299 tengo mis metodos de ordenamiento que ya se habian realizo con anterioridad 
#Defino mi metodo quicksort en el cual divido mi arreglo en 2 en chaparrines y garruchines y estos se comparan y si hay un garruchin en el area de chaparrins, este se intercambia al lado de los garruchines y esto lo hace hasta ordenarlo totalmenteç
#De esta manera el metodo Quicksort lo considero como el mas rapido para ordenar
def QuickSort(a, izquierda, derecha):

	k = izquierda
	j = derecha

	pivote = a[int((izquierda+derecha)/2)]

	while k <= j:
		while a[k] < pivote:
			k += 1
		while a[j] > pivote:
			j -= 1
		if k <= j:
			aux = a[k]
			a[k] = a[j]
			a[j] = aux
			k += 1
			j -= 1	
	if j > izquierda:
		QuickSort(a, izquierda, j)
	if k < derecha:
		QuickSort(a, k, derecha)
	return a
#Defino mi metodo de shellsort que es otro metodo de ordenamiento para el cuando este va comparando por saltos en el arreglo
#Si tienes un arreglo de 12 lo divides entre 2 y te da 6 y cada 6 hace un comparacion, cada que se terminen de hacer las comparaciones, se vuelve a dividir el arreglo y se hace lo mismo del salto cada 3

def ShellSort(array):
	brinco = int(len(array)/2)

	while brinco > 0:
		k = brinco
		if k < len(array):
			for k in range(len(array)):
				j = k - brinco
				while j >= 0:
					i = j + brinco
					if array[j] <= array[i]:
						j -= 1
					else:
						aux = array[j]
						array[j] = array[i]
						array[i] = aux
						j -= brinco
		brinco = int(brinco/2)
	return array

#Función que realiza el ordenamiento 'merge'
def MergeSort(Array):
	longitudtotal_Array = len(Array)
	#Primer división del array principal
	pibote = int(len(Array)/2)
	#Arreglo para la parte izquierda del arreglo
	left = []
	#Arreglos que dividen la parte izquierda ya dividida
	lenleft_l = []

	lenleft_r = []

	#Arreglo para la parte derecho del arreglo
	right = []

	#Arreglos que dividen la parte derecho ya dividida
	lenright_l = []

	lenright_r = []

	#Contador que guia el acceso al arreglo original
	i = 0

	#Llenado del arreglo que representa a parte izquerda
	for j in range(pibote):
		left.insert(j,Array[i])
		del(Array[i])


	#Llenado del arreglo que representa a parte derecha

	for j in range(pibote):
		right.insert(j,Array[i])

		del(Array[i])

	#Separación de la parte izquierda del arreglo en otras dos partes pasando primero el llamado 'pibote', que nos servira para partir a la mitad esta parte del arreglo
	pibotel = int(len(left)/2)
	i = 0

	#iteración donde se llena la división izquierda
	for x in range(pibotel):
		lenleft_l.insert(x,left[i])
		i += 1

	#iteración donde se llena la división derecha
	for x in range(pibotel,len(left)):
		lenleft_r.insert(x,left[i])
		i += 1

	#Separación de la parte derecha del arreglo en otras dos partes pasando primero el llamado 'pibote', que nos servira para partir a la mitad esta parte del arreglo
	piboter = int(len(right)/2)
	i = 0

	#iteración donde se llena la división derecha, de la división ya realizada antes.
	for x in range(piboter):
		lenright_l.insert(x,right[i])
		i += 1

	#iteración donde se llena la división izquierda, de la división ya realizada antes.
	for x in range(piboter,len(right)):
		lenright_r.insert(x,right[i])
		i += 1

	#En esta iteración se acomoda la parte izquierda de la primera particion del lado izquierdo
	for i in range(0,len(lenleft_l)-1):
		for j in range(0,len(lenleft_l)-1-i):
			if lenleft_l[j] > lenleft_l[j+1]:
				lenleft_l[j],lenleft_l[j+1] = lenleft_l[j+1],lenleft_l[j]


	#En esta iteración se acomoda la parte derecha de la primera particion del lado izquierdo
	for i in range(0,len(lenleft_r)-1):
		for j in range(0,len(lenleft_r)-1-i):
			if lenleft_r[j] > lenleft_r[j+1]:
				lenleft_r[j],lenleft_r[j+1] = lenleft_r[j+1],lenleft_r[j]

	#En esta iteración se acomoda la parte izquierda de la primera particion del lado derecho
	for i in range(0,len(lenright_l)-1):
		for j in range(0,len(lenright_l)-1-i):
			if lenright_l[j] > lenright_l[j+1]:
				lenright_l[j],lenright_l[j+1] = lenright_l[j+1],lenright_l[j]

	#En esta iteración se acomoda la parte derecha de la primera particion del lado derecho			
	for i in range(0,len(lenright_r)-1):
		for j in range(0,len(lenright_r)-1-i):
			if lenright_r[j] > lenright_r[j+1]:
				lenright_r[j],lenright_r[j+1] = lenright_r[j+1],lenright_r[j]

	#indices que serán utilizados en la siguiente iteración
	l = 0
	r = 0

	#En este ciclo se van a comparar las dos mitades del lado izquierdo, y serán acomodadas en orden en el arreglo que representa la mitad izquierda del arreglo original

	#El ciclo se realiza con el rango(tamaño) del arreglo que representa la parte izquierda del arreglo original
	for i in range(len(left)):
		#En esta condición se pregunta si el rango de las dos mitades a comparar es mayor a 0, para poder comparar los datos en ellos, si no lo es, pasara al 'else', donde introducira los datos sobrante(que tambien serán os mayores), en el arreglo donde los estamos acomodando
		if len(lenleft_l) > 0 and len(lenleft_r) > 0:
			#Aqui se comparan los datos en el indice actual de ambos arreglos, si se cumple la condición de que el dato de 'l' sea menor que el de 'r', el dato que de 'l' pasara al arreglo en donde estamos acomodando los datos 
			if lenleft_l[l] < lenleft_r[r]:
				#Se introduce el dato de 'l' al arreglo en donde se están acomodando los datos.
				left[i] = lenleft_l[l]
				#El dato que introducimos al nuevo arreglo es eliminado de su arreglo original
				del(lenleft_l[l])					
			#Si no se cumple la condción anterior, se pasara a esta parte, y en vez de pasar el dato de 'l', al nuevo arreglo, hará las operaciones con el dato en el arreglo 'r'
			else:	
				left[i] = lenleft_r[r]
				del(lenleft_r[r])

	#En este ciclo se van a comparar las dos mitades del lado derecho, y serán acomodadas en orden en el arreglo que representa la mitad derecha del arreglo original

	#Se hace lo mismo que en el ciclo anterior, con la diferencia que aquí se realizaran los operaciones con la mitad derecha del arreglo original

	for i in range(len(right)):
		if len(lenright_l) > 0 and len(lenright_r) > 0:
			if lenright_l[l] < lenright_r[r]:
				right[i] = lenright_l[l]
				del(lenright_l[l])
			else:
				right[i] = lenright_r[r]
				del(lenright_r[r])

	#Ordenación final

	for i in range(longitudtotal_Array):		
		if len(left) > 0 and len(right) > 0:		
			if left[l] < right[r]:
				Array.insert(i,left[l])
				del(left[l])		
			else:		
				Array.insert(i,right[r])
				del(right[r])
		else:
			if len(left) == 0:
				Array.insert(i,right[r])
				del(right[r])
			elif len(right) == 0:
				Array.insert(i,left[l])
				del(left[l])

	print("-"*150)
	print("Listo",Array)
	print("-"*150)
	return Array

#Agrego mi metodo de la burbuja ya realizado anteriormente para poder llamarlo en instrucciones futuras, este es un ordenamiento sencillo en el cual
#Va comparando los numeros y si uno es mayos que otro lo intercambio, y eso lo hace recorriendo un arreglo varias veces para poder hacer las comparaciones
def Burbuja(array):
	for i in range(0, len(array)-1):
		for j in range(0, len(array)-1-i):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

#Las siguientes palabras que estan sirven para haccer las operaciones en donde declaro una varible y la igualo a mi metodo datatime.now
promedio_Quicksort = datetime.now()
promedio_Quicksort = promedio_Quicksort - promedio_Quicksort
promedio_Shellsort = datetime.now()
promedio_Shellsort = promedio_Shellsort - promedio_Shellsort
promedio_Merge = datetime.now()
promedio_Merge = promedio_Merge - promedio_Merge
promedio_bubble = datetime.now()
promedio_bubble = promedio_bubble -promedio_bubble

#Aqui uso un for en el cual mandare a llamar las instrucciones de datetime para poder realizar las opreaciones y los promedios, de igual manera
#Cada metodo de ordenamiento de iguala a uno de los array que puse en el metodo arreglos para poder ordenarlos
for i in range(1,31):
	n = i

	#Aqui se utiliza el Quicksort
	Quicksortarray = Arreglos(i)
	k = 0
	muestra = []
	for j in range(0,10):

	 	muestra.insert(j,Quicksortarray[k])
	 	k += 1

	print("Pedazo de arreglo utilizado del ordenamiento", muestra)

	tiempoinicial_Quicksort = datetime.now()

	QuickSort(Quicksortarray, 0, len(Quicksortarray)-1)

	tiempofinal_Quicksort  = datetime.now()

	tiempototal_Quicksort = tiempofinal_Quicksort - tiempoinicial_Quicksort

	promedio_Quicksort += tiempototal_Quicksort

	#Aqui se utiliza el Shellsort

	array = Arreglos(i)

	tiempoinicial_shellsort = datetime.now()

	ShellSort(array)

	tiempofinal_Shellsort = datetime.now()

	tiempototal_Shellsort = tiempofinal_Shellsort - tiempoinicial_shellsort

	promedio_Shellsort += tiempototal_Shellsort

	#Aqui utilizo el merge

	array = Arreglos(i)

	tiempoinicial_Mergesort = datetime.now()

	MergeSort(array)

	tiempofinal_Mergesort = datetime.now()

	tiempototal_Mergesort = tiempofinal_Mergesort - tiempoinicial_Mergesort

	promedio_Merge += tiempototal_Mergesort

	#Aqui utilizo el bubble

	array = Arreglos(i)

	tiempoinicial_Bubble = datetime.now()

	Burbuja(array)

	tiempofinal_Bubble = datetime.now()

	tiempototal_Bubble = tiempofinal_Bubble - tiempoinicial_Bubble

	promedio_bubble += tiempototal_Bubble

	print("-"*150)
	print("Prueba No. : ", i)
	print("-"*150)
	print("Algoritmo ordenamiento   -  Tiempo Ordenamiento")
	print("-"*150)
	print("Quicksort ", tiempototal_Quicksort)
	print("-"*150)
	print("Shellsort ", tiempototal_Shellsort)
	print("-"*150)
	print("Merge     ", tiempototal_Mergesort)
	print("-"*150)
	print("Burbuja   ", tiempototal_Bubble)

print("-"*150)
print("Algoritmo ordenamiento   -  Tiempo Promedio Ordenamiento")
print("-"*150)
print("Quicksort", promedio_Quicksort/30)
print("-"*150)
print("Shellsort", promedio_Shellsort/30)
print("-"*150)
print("Merge    ", promedio_Merge/30)
print("-"*150)
print("Burbuja  ", promedio_bubble/30)
print("-"*150)
