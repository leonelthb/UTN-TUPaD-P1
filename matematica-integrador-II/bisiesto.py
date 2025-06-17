from datetime import datetime
from itertools import product

# Función que determina si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Pedimos cuántas personas hay en el grupo
cantidad = int(input("¿Cuántas personas hay en el grupo? "))

# Creamos una lista para guardar los años de nacimiento
anios = []

# Ingresamos los años uno por uno
for i in range(cantidad):
    anio = int(input(f"Ingresá el año de nacimiento del integrante {i + 1}: "))
    anios.append(anio)

# Contamos pares e impares
pares = 0
impares = 0
for anio in anios:
    if anio % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nCantidad de años pares: {pares}")
print(f"Cantidad de años impares: {impares}")

# Verificamos si todos nacieron después del 2000
if all(anio > 2000 for anio in anios):
    print("Grupo Z")

# Verificamos si alguno nació en un año bisiesto
if any(es_bisiesto(anio) for anio in anios):
    print("Tenemos un año especial")

# Calculamos edades actuales
anio_actual = datetime.now().year
edades = [anio_actual - anio for anio in anios]

# Mostramos las edades
print(f"\nEdades actuales: {edades}")

# Producto cartesiano entre años y edades
print("\nProducto cartesiano (año, edad):")
for combinacion in product(anios, edades):
    print(combinacion)
