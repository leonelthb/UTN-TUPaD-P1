# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 


for num in range (1,101):
    print(num)


# Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 


numero = input("Ingresa un número entero: ")

if numero.startswith('-'):
    numero = numero[1:]
cantidad_digitos = len(numero)
print("El número tiene", cantidad_digitos, "dígitos.")

# Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

inicio = min(a, b)
fin = max(a, b)

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("La suma de los números entre", inicio, "y", fin, "es:", suma)

# Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
suma_total = 0
while True:
    numero = int(input("Ingresa un número entero preciosa 0 para finalizar): "))
    if numero == 0:
        break  # Salir del bucle si el usuario ingresa 0
    suma_total += numero  
print("La suma total de los números ingresados es:", suma_total)


# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
numero_secreto = random.randint(0, 9) #para un numero random entre 0 y 9

intentos = 0  

print("Adivina el numero entre 0 y 9!")

while True:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        print("Felicidades adivinaste el numero en", intentos, "intento/s")
        break
    else:
        print("Intenta de nuevo.")


# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for num in range (100, -1 , -1): #Rango de 100 a 0 decreciente
    if num % 2 == 0: # Para los numeros pares
        print(num)


# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 


n = int(input("Ingresa un número entero positivo: ")) # Solicitar que ingrese numero positivo
if n < 0: #Verificar que el numero sea positivo
    print("Ingresa un número positivo.") #En caso que no, imprimir que ingrese un positivo
else:
    suma = 0
    for i in range(0, n + 1):
        suma += i
    print("La suma de los números de 0 hasta", n, "es:", suma)


# Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

#  Se cambio la cantiadad de numero ya esta comprobado
cantidad_numeros = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Pedir los números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))

    # pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# resultados
print("\nResultados:")
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)




# Ejercicio 9:  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).
# Cantidad de numeros puede ser modificado
cantidad_numeros = 100

suma_total = 0  # Acumulador

# Pedir los números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma_total += numero

# Calcular la media
media = suma_total / cantidad_numeros

# Imprimir el resultado
print("\nLa media de los", cantidad_numeros, "números ingresados es:", media)


#Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

# Pedir al usuario que ingrese un número
numero = input("Ingresa un número entero: ")

# Invertir el número usando slicing
numero_invertido = numero[::-1]

# Mostrar el resultado
print("El número invertido es:", numero_invertido)

