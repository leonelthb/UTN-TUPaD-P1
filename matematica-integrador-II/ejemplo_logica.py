# Diccionario que almacena las claves y sus valores
alumnos = {
    "ALEX": 42209093,
    "LEONEL": 36185972,
    "GINO": 47527332,
    "CHRISTIAN": 30975414,
    "AGUSTÍN": 44347575
}

# la funcion que determina si es par o impar
def es_impar(dni): 
    return dni % 2 != 0

# Ciclo for para evaluar cada DNI de los alumnos y determinar cuales son par e impar
for nombre, dni in alumnos.items(): # items devuelve pares clave-valor (nombre y el dni) 
    print(f"{nombre}: DNI = {dni} > > >  {'Impar (True)' if es_impar(dni) else 'Par (False)'}") # imprime si es par o impar usando el formato F-strings, llama a es_impar
    # si es impar devuelve True, sino False