def fibonaci(fib):
    a = 0
    b = 1

    for i in range (fib):
        c = a + b
        a = b
        b = c

    return b

#print(fibonaci(5))

#con un while
a = 0
b = 1

c = 0
d = int(input("Ingresa el numero de digitos que deseas generar: "))

while c < d:
    e = a + b
    a = b
    b = e
    print(e)

    c = c + 1