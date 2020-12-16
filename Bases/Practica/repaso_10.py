#lista = [7, 9, 7, 23, 4, 53]
#lista.insert(2, 98)
#print(lista)

lista = []
cantidad = int(input("Ingresa el numero de elementos que va atener la lista: "))
for i in range(0, cantidad):
    elementos = int(input("Ingresa un elemento: "))
    lista.append(elementos)
    print(lista)
