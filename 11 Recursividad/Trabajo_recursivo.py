# Ejercicio 1
# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 


def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    

if __name__ == "__main__":
    print(factorial(5))





# Ejercicio 2
# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1) + fibonacci_recursivo(posicion-2)
    

if __name__ == "__main__":
    print(fibonacci_recursivo(7)) 




    # Ejercicio 3
#  Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 


def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m -1)
    
print(potencia(2,3))




# Ejercicio 4
# Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
def decimal(n):
    if n == 0:
        return "" 
    else:
        return decimal(n // 2) + str(n % 2) 
    
def convertir_a_binario(n):
    if n == 0:
        return "0"
    else:
        return decimal(n)

n = int(input("Ingresa un numero entero positivo: "))

if n < 0:
    print("Ingresa un numero positivo")
else: 
    print(f"El numero {n} en binario es: {convertir_a_binario(n)}")




# Ejercicio 5
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
#     Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed().


def palindromo(palabra):
    # Para el caso base, si tiene 0 o 1, es palindromo
    if len(palabra) <= 1:
        return True
    # Comparar la primera y ultima letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la subcadena sin la primera y ultima letra

    return palindromo(palabra[1:-1])

print(palindromo("reconocer"))




# Ejercicio 6
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
#     Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 







def suma(n):
    # caso base, si n<10, se considera un solo digito
    if n < 10:
        return (n)
    return (n % 10) + suma(n // 10) # para obtener el ultimo 
print(suma(1234))





# Ejercicio 7
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 

#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 

#      Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def bloques(n):
    #Caso base,si n es 1, es un solo bloque
    if n == 1:
        return 1
# paso recursivo, n bloques en el nivel actual + bloques de los niveles superiores
    return n + bloques(n - 1)

print(bloques(2))




# Ejercicio 8
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
#     Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5)


def contar(numero,digito):
    # Caso base, si el numero es 0, no se cuenta
    if numero == 0:
        return 0
    if numero % 10 == digito: #se compara el ultimo digito con el digito buscado
        return 1 + contar(numero // 10, digito)
    else:
        return contar(numero // 10, digito)
    



print(contar(12233421, 2))