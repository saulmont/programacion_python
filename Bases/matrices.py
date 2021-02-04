# MATRICES

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    print(fila)

print(matriz[1][1])

lista = matriz[1]
print(lista[1])

# Crear una matriz

n = int(input('Ingrese un numero: '))
matrix = []


# for i in range(n):
#     matrix.append([0 for j in range(n)])

for i in range(n):
    matrix.append([0] * n)


for fila in range(n):
    for columna in range(n):
        matrix[fila][columna] = int(input('Ingrese un valor en la posicion ({}, {}): '.format(fila, columna)))

for fila in matriz:
    print(fila)