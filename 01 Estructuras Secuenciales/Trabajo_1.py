#Ejercicio 1 
print("hola mundo")

#ejercicio 2
nombre = input ("Ingrese su nombre ")

print(f" Hola! {nombre}")


#Ejercicio 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingresa tu apellido: ")
edad = input ("ingresa tu edad: ")
residencia = input ("Lugar de residencia?: ")

print (f"soy {nombre} {apellido}, tengo {edad}, y vivo en {residencia}  ")


#Ejercicio 4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 

#calcular el area de un circulo
radio = float(input("Ingrese el radio del radio: "))
pi = 3.14
area = pi * radio ** 2
perimetro = 2 * pi * radio 

#mostrar el resultado
print("EL area es de ", area)
print("El perimetro es de ", perimetro)

#Ejercicio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

input("Ingrese una cantiadad de segundos")

#Ejercicio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))

hora = segundos // 3600 # 1 hora = 3600''
segundos_restantes = segundos % 3600 #el resto de segundos 
minutos = segundos_restantes // 60 #1 min = 60 seg
segundos_f = segundos_restantes % 60 #resante de segundos

print(f"Los {segundos} equivalen a {hora} horas, {minutos} minutos y {segundos_f} segundos ")

#Ejercicio 6
#  Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.  

numero = int(input("Ingrese el numero que quiere multiplicar ")) #se le solicita el numero al usuario que quiere 

print("por 2: ",2 * numero )
print("por 3: ",3 * numero )
print("por 4: ",4 * numero )
print("por 5: ",5 * numero )
print("por 6: ",6 * numero )
print("por 7: ",7 * numero )
print("por 8: ",8 * numero )
print("por 9: ",9 * numero ) 

#Ejercicio 7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numero1 = int(input("Ingrese el primer numero entero: ")) #Ingreso del 1ro numero
numero2 = int(input("Ingrese el segundo numero entero: "))#Ingreso del 2do numero

#Formulas e imprimir en pantalla el resultado
print("multiplicandolos: ", numero1 * numero2)
print("Sumandolos: ", numero1 + numero2)
print("Dividiendolos: ", numero1 / numero2)
print("Restandolos: ", numero1 - numero2)

#Ejercicio 8
 #Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo: ICM = peso/altura  

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))

IMC = peso / (altura ** 2)

print("Tu IMC es de ", str(IMC))

#Ejercicio 9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# ��𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/ 5 .𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32

celcius = float(input("Ingrese la Temperatura en Celcius: "))
farhrenheit = 9/5 * celcius + 32

print("La Equivalencia a Farhrenheit es de ", farhrenheit, "Grados")

#Ejercicio 10 
#Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.

numero1 = float(input("Ingresa el primero nuermo: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print("El promedio es de ", promedio)