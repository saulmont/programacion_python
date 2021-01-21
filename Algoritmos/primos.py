n = int(input("Ingresa un numero: "))
c = 0
i = 1
while i < n:
    if n % i == 0:
        c = c + 1
    i = i + 1

if c > 2:
    print("No es primo")

else:
    print("Es primo")