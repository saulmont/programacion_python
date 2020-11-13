# BUCLE WHILE

"""
Un bucle while es el que se repite/ejecuta siempre que se cumpla con una condicion.

Ejemplo:

    while condicion:
        ###BLOQUE CODIGO###
    else:
        ###FIN DE LA EJECUCION###
"""

contador = 0
limite = 5

pares = []
impares = []

while contador <= limite: # Condicion de ejecucion.
    print("Valor del contador:", contador)
    
    # El operador %(modulo) muestra o recupera el residuo de una division.
    if contador % 2 == 0: # Verifica que el contador sea un numero par.
        print("{} es un numero par".format(contador))
        pares.append(contador) # Agrega el numero par a la lista de numeros pares.
    else: # En caso de no ser par.
        print("{} es un numero impar".format(contador))
        impares.append(contador) # Agrega el numero a la lista de numeros impares.

    contador = contador + 1

else: # Se ejecuta cuando el bucle cumple con la condicion.

    print("El bucle se termino de ejecutar.")
    print(pares)
    print(impares)
