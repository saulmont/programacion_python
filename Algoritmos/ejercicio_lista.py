def es_primo(n):
    c = 0
    i = 1
    while i <= n:
        if n % i == 0:
            c = c + 1
        i = i + 1

    if c > 2:
        return False
    else:
        return True

if __name__ == '__main__':

    lista = []
    contador = 0

    cantidad = int(input("Ingresa el numero de elementos que va a tener la lista:  "))

    while contador < cantidad:
        elemento = int(input("Ingresa un elemento: "))
        if es_primo(elemento):
            lista.append(elemento)
            contador = contador + 1
        else:
            print("Ese numero no es primo")

    print(lista)