num = int(input("Ingresa un numero: "))
acu = 1

while num > 1:
    acu = acu * num
    num = num - 1

print("Resultado: ", acu)