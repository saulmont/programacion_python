# BUCLE FOR

"""
Un bluce for se ejecuta un numero limitado de veces segun el rango que se le indique.

Ejemplo:
    for indice in rango_de_valores:
        print(indice)
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Formas de imprimir los elementos de una lista con 
# un bucle for:

# 1. Primera forma

for elemento in lista:
    print(elemento)

# 2. Segunda forma

elementos_lista = len(lista)

for indice in range(0, elementos_lista):
    print("Indice:", indice, "Elemento lista:", lista[indice])

# Imprimiendo una cadena de texto como una lista.

cadena_texto = "Saúl"

for caracter in cadena_texto:
    print(caracter)
