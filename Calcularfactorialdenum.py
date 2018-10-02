num = int(input("Ingresa un numero: ")) //Aqui mando a pedir un numero en cual se calculara su factorial
factorial = 1
for i in range(num):
    print (factorial, " * " , num)
    factorial = factorial * num
    num = num - 1 

print (factorial)
    
    
