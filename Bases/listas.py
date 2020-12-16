# ARREGLOS/VECTORES/LISTAS

""" 
Las listas pueden recibir cualquier tipo de dato(caracteres, cadenas de texto, numeros enteros y decimales, boleanos).
Las listas pueden ser facilmente modificadas.
Para crear una lista se utilizan los corchetes [].
"""

lista = ['a', 'b', 'c', "Hola", "Mundo", 1, 2, 3, 4.4, 5.5, True]

# Mostrar la cantidad de elementos que posee una lista.
elementos = len(lista)

print(elementos)

# Agregar nuevo elemento al final de la lista
lista.append(False)
print(lista)

# Agregar elemento en una posicion de la lista
lista.insert(0, "Gato")
print(lista)

# Eliminar un elemento de la lista
lista.remove('c')
print(lista)

#Elimina el ultimo elemento de la lista
ultimo_elemento = lista.pop()
print(lista, ultimo_elemento)

# ORDENANDO ELEMENTOS DE UNA LISTA

lista_numeros = [9, 5, 4, 6, 0, 7, 2, 1, 8, 3]

# Imprimer la lista sin ordenar
print(lista_numeros)

# Ordena los numeros en la lista de menor a mayor
lista_numeros.sort()

# Imprimer la lista ordenada
print(lista_numeros)

# Ordena los numeros en la lista de mayor a menor
lista_numeros.sort(reverse=True)

# Imprime la lista ordenada
print(lista_numeros)

# Unir dos listas
nueva_lista = [10, 11, 12, 13, 14]

# Uniendo las listas
lista_numeros.extend(nueva_lista)

print(lista_numeros)
