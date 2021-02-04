matriz = []

n = int(input('Ingrese un numero: '))

for i in range(n):
    matriz.append([0] * n)


fila = 0
while fila < n:
    columna = 0
    while columna < n:
        matriz[fila][columna] = int(input("Ingrese un valor en la pocision ({}, {}): ".format(fila, columna)))
        columna = columna + 1
    fila = fila + 1


fila = 0
while fila < n:
    print(matriz[fila])
    fila = fila + 1