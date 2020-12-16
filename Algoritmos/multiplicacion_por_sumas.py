numero = int(input("Ingresa un numero: "))
multiplicando = int(input("Ingresa un multiplicando: "))
acumulador = 0
contador = 0

while contador < multiplicando:
    acumulador = acumulador + numero
    contador = contador + 1

print("Resultado:", acumulador)