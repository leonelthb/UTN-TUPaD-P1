#Ejercicio 1: Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Definición de la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal

imprimir_hola_mundo()






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






# Ejercicio 2:Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta funcion desde el programa principal solicitando el nombre al usuario.



# Definir la función saludar_usuario
def saludar_usuario(nombre): # Toma el parametro "nombre"
    return f"Hola {nombre}!"

# Programa principal
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






# Ejercicio 3: Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# pedir los datos al usuario y llamar a esta función con los valores in
# gresados.

# Definicion de Variables
def informaicon_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre}, {apellido}, de {edad} años y soy de {residencia}")

# Programa principal

name_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input ("Ingrsa tu apellido: ")
edad_usuario = int(input("Ingresa tu edad: "))
residencia_usuario = input("Donde vives?? ")

informaicon_personal(name_usuario, apellido_usuario, edad_usuario, residencia_usuario)





# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






# Ejrecicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar 
# ambas funciones para mostrar los resultados

# Declaracion de funciones
PI = 3.14
def calcular_area_cirulo(radio): # Funcion para calcular el area
    return PI * radio ** 2

def  calular_perimetro_circulo(radio): # Funcion para calcular el perimtro
    return 2 * PI * radio   

# Programa principal

radio_usuario = float(input("Introduce el radio de un circulo: ")) # Ingreso del radio 
area = calcular_area_cirulo(radio_usuario)
perimetro = calular_perimetro_circulo(radio_usuario) 

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del cirulo es: {perimetro:.2f}")







# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






    # Ejercicio 5: Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y 
# mostrar el resultado usando esta función.

# Definicion de funcions
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Programa principal 
segundos_usuario = int(input("Ingresa una cantidad de segundos: "))
horas = segundos_a_horas(segundos_usuario) # Llamar a la funion segundos_a_horas para el resultado
print(f"{segundos_usuario} segundos equivalents a {horas:.2f} horas.") # Mostrar resultado, .2f formatear el numero con 2 decimales






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@







    # Ejercicio 6: Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.


# Definicion de variables
def tabla_multi(numero):
    for i in range (1,11): # para que multiplique del 1 al 10
        print(f"{numero} x {i} = {numero * i}") 
# Programa principal 
numero_usuario = int(input("Ingresa un numero que quieras multiplicar: "))
tabla_multi(numero_usuario) # Llamamos a la funcion






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@







# Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# Definicion de variables

def operaciones_basicas(a,b): # asegurarse que el valor de los variables se puedan dividir entre si 
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No pueden divir por 0"

    return (suma, resta, multiplicacion, division) #devolucion de los resultados

# Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# Definicion de variables
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multipliacion = a * b

    if b != 0:
        division = a / b
    else:
        division = None

    return (suma, resta, multipliacion,division)

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingresa el valor de b: "))

suma, resta, multiplicacion, division = operaciones_basicas(a,b)

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ",multiplicacion)
if division is not None:
    print("Division: ", division)
else:
    print("No se puede dividir por 0")








# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






# Ejerecicio 8: Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la funcion
# para mostrar el resultado con dos decimales


# Definicion de variables
def calcular_imc(peso, altura):
    imc = peso / (altura * 2)
    return round(imc, 2) # redondear el IMC en 2 decimales para mostrar


# Programa principal 
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))
#Llamar a la funcion
IMC = calcular_imc(peso, altura)
print(f"Tu IMC es de {IMC}")






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.



# Definicion de las variables
def celcuis_a_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32 # Formula para convertir de C a F
    return  fahrenheit# Devulve el valor 

# Programa principal 
celcius = float(input("Ingrese la temperatura en grados celcius: "))
fahrenheit = celcuis_a_fahrenheit(celcius)
print(f"La conversion de grados Celcius a Fahrenheit es de: {fahrenheit}°F .")






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






# Ejercicio 10: Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


# Definicion de variables
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3 # Calcular el promedio
    return promedio # Devolver el resultado

# Programa principal
# Valor de las variables
a = float(input("Ingrese la primera nota: "))
b = float(input("Ingrese la segunda nota: "))
c = float (input("Ingrese la tercera nota: "))

promedio = calcular_promedio(a, b, c) #Llamar a la funcion
print(f"El promedio es de {promedio:.2f}") #Imprimir resultado










