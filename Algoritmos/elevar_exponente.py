base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

acumulador = 1
contador = 0

if exponente == 0:
    print("El resultado es: ", exponente)

else:
    while contador < exponente:
        acumulador = acumulador * base
        contador = contador + 1
    print("El resultado es: ", acumulador)
     