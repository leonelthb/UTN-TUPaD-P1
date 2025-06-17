# Ingreso de los DNIs (reales o ficticios).
def ingreso_dni():
    lista = []
    continuar = "s"    
    while continuar == "s" or continuar == "S":
        documento = int(input("Ingrese un DNI: "))
        lista.append(documento)
        continuar = input("¿Desea continuar? S o N: ").strip()
    return lista
      
# documentos= [42209093, 36185972, 47527332, 30975414, 44347575]

# Generación automática de los conjuntos de dígitos únicos.
def digitos_unicos(lista):
    lista_conjuntos=[]
    for i in lista:
        conjunto = set()
        for d in str(i):
            conjunto.add(int(d))
        lista_conjuntos.append(conjunto)
    return lista_conjuntos

# Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
def vista_conjuntos(listadeconjuntos):
    conjunto_resultados = {"union": set(),
                            "interseccion": set(),
                            "diferencias": set(),
                            "diferencia simetrica": set()
                            }
    conjunto_resultados["union"] = set.union(*listadeconjuntos)
    conjunto_resultados["interseccion"] = set.intersection(*listadeconjuntos)
    conjunto_resultados["diferencias"] = diferencia(listadeconjuntos)
    conjunto_resultados["diferencia simetrica"] = diferencia_simetrica(listadeconjuntos)
    print("Unión:", conjunto_resultados["union"])
    print("Intersección:", conjunto_resultados["interseccion"])
    print("Diferencias:", conjunto_resultados["diferencias"])
    print("Diferencia Simétrica:", conjunto_resultados["diferencia simetrica"])
    print("_" * 30)

def diferencia(listaconjuntos):
    acumulador = listaconjuntos[0]
    for i in range(1, len(listaconjuntos)):
        acumulador = acumulador - listaconjuntos[i]
    return acumulador

def diferencia_simetrica(listaconjuntos):
    acumulador = listaconjuntos[0]
    for i in range(1, len(listaconjuntos)):
        acumulador = acumulador ^ listaconjuntos[i]
    return acumulador

# Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
def frecuencia(lista_dnis):
    for dni in lista_dnis:
        print(f"DNI: {dni}")
        print("Frecuencia de dígitos:")
        conteo = {}  # diccionario para contar los dígitos
        for digito in str(dni):
            if digito in conteo:
                conteo[digito] += 1
            else:
                conteo[digito] = 1
        for digito, cantidad in conteo.items():
            if cantidad == 1:
                veces = "vez"
            else:
                veces = "veces"
            print(f"   Dígito {digito} → {cantidad} {veces}")
        print("-" * 30)

# Suma total de los dígitos de cada DNI.
def suma_digitos(lista_dnis):
    for dni in lista_dnis:
        suma = 0
        for digito in str(dni):
            suma += int(digito)
        print(f"Suma de los dígitos del DNI {dni}: {suma}")
    print("_" * 30)

# Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
def condiciones_logicas(listaconjuntos):
    digitos_compartidos = set.intersection(*listaconjuntos)

    if digitos_compartidos:
        print(f"Dígito(s) compartido(s) en todos los conjuntos: {digitos_compartidos}")
    else:
        print("No hay dígitos compartidos en todos los conjuntos.")

    hay_diversidad_alta = False
    for conjunto in listaconjuntos:
        if len(conjunto) > 6:
            hay_diversidad_alta = True

    if hay_diversidad_alta:
        print("Diversidad numérica alta: algún conjunto tiene más de 6 elementos.")
    else:
        print("No hay diversidad numérica alta.")

    if len(digitos_compartidos) == 1:
        print("Hay un dígito representativo del grupo (intersección con un solo elemento).")




dnis_ingresados = ingreso_dni()


conjuntos_generados = digitos_unicos(dnis_ingresados)


vista_conjuntos(conjuntos_generados)

frecuencia(dnis_ingresados)

suma_digitos(dnis_ingresados)

condiciones_logicas(conjuntos_generados)