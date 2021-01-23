lista = []
cantidad = int(input("Ingresa el numero de elementos que va a tener la lista: "))

for i in range(0, cantidad):
    elementos = int(input("Ingrese el numero de elementos que va a tener la lista: "))
    lista.append(elementos)

tam = len(lista)
suma = 0

for i in lista:
    suma = suma + i

promedio = suma / tam

print("El promedio es:", promedio)