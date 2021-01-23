lista = []
cantidad = int(input("Ingresa el numero de elementos que va a tener la lista: "))
for i in range(0, cantidad):
    elementos = int(input("Ingresa los elementos de la lista: "))
    lista.append(elementos)
    print(lista)

for i in range(cantidad-1, -1,-1):
    print (lista[i])

for i in range(0, cantidad):
    print(lista[i])