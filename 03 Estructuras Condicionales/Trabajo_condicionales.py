#Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")



#Ejecircio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

nota = int(input("Ingrese una nota: "))
if nota >= 6:
    print("Estas aprobado")
else:
    print("Estas desaprobado")

#Ejercicio 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar. 

numero = int(input("Ingrese un numero par"))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingresa un numero inpar")

#Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.


edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Eres un niño")
elif (edad >= 12) and (edad < 18):
    print("Eres un Adolecenrte")
elif (edad >= 18) and (edad < 30):
    print("Eres un Adulto/a joven")
else:
    print("Eres un adulto/a")


#Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.


contraseña = input("Introduce una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6:
import random
from statistics import mode, median, mean 


numeros_aleatorios = [random.randint(1, 100) for i in range(100)]


moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


print(f"Numeros aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")


if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

#Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.

    texto = input("Ingrese una frase o palabra ")
if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)

#Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 


nombre = input("Ingresa tu nombre ")

print("Eligue una opcion")
print("Opcion 1 si queres el nombre en mayuscula")
print("Opcion 2 si queres el nombre en minusculas")
print("Opcion 3 si queres la primera letra con Mayus")


opcion = input("Ingresa 1, 2, 3" )

if opcion == "1":
    nombre_transformado = nombre.upper()
elif opcion == "2":
    nombre_transformado = nombre.lower()
elif opcion == "3":
    nombre_transformado = nombre.title()
else: 
    nombre_transformado = "Opcion no valida"


print("Resultado", nombre_transformado)


#Ejercicio 9 Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

mangnitud = int(input("Ingresa la magnitud del terremoto "))
if mangnitud < 3:
    print("Muy leve")
elif mangnitud >= 3 and mangnitud < 4:
    print("Leve, Ligeramente perceptible")
elif mangnitud >= 4 and mangnitud < 5:
    print("Moderado, sentido por personas, no genera daños")
elif mangnitud >= 5 and mangnitud < 6:
    print("Fuerte, puede causar daños en estructuras debiles")
elif mangnitud >= 6 and mangnitud < 7:
    print("Muy Fuerte, puede causar daños significativos")
elif mangnitud  > 7:
    print("Extremo, puede causar graves daños a gran escala")


#Ejercucio 10: 
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1 para enero, 2 para febrero, ..., 12 para diciembre): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Comprobar la estación según el hemisferio
if hemisferio == "N":  # Hemisferio Norte
    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3 and (mes != 3 or dia <= 20)):  
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 6 and (mes != 6 or dia <= 20)):  
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 9 and (mes != 9 or dia <= 20)):  
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes >= 10 and mes <= 12 and (mes != 12 or dia <= 20)):  
        estacion = "Otoño"
elif hemisferio == "S":  # Hemisferio Sur
    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3 and (mes != 3 or dia <= 20)):  
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 6 and (mes != 6 or dia <= 20)): 
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 9 and (mes != 9 or dia <= 20)):  
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes >= 10 and mes <= 12 and (mes != 12 or dia <= 20)):  
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Imprimir la estación del año
print(f"En el hemisferio {hemisferio}, el día {dia} de {mes} corresponde a la estación: {estacion}")

