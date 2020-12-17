dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))
contador = 0

if divisor == 0:
    print("El resultado de cualquier numero deividido para cero es cero")

else:
    while dividendo > 1:
        dividendo = dividendo - divisor
        contador = contador + 1
    print("El resultado es: ",contador)