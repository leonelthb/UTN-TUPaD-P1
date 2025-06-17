# Diccionario original: países → capitales
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokio",
    "Alemania": "Berlín",
    "Chile": "Santiago",
    "España": "Madrid",
    "Italia": "Roma",
}

capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

print("\nDiccionario original (país >> capital):")
print(paises_a_capitales)

print("\nDiccionario invertido (capital >> país):")
print(capitales_a_paises)
