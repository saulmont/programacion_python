def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def division(a, b):
    if b == 0:
        print("Cualquier numero dividido para 0 es cero")
    else:
        resultado = a / b
        return resultado

if __name__ == "__main__":
    opcion = 0
    while opcion < 5:
        print("")
        print("1.suma")
        print("2.resta")
        print("3.multiplicacion")
        print("4.divison")
        print("5.salir")
        opcion = int(input("Escoge una opcion: "))

        if opcion == 1:
            a = int(input("Ingresa un numero: "))
            b = int(input("Ingresa otro numero: "))
            s = suma(a, b)
            print("El resultado es: ", s)

        if opcion == 2:
            a = int(input("Ingresa un numero: "))
            b = int(input("Ingresa otro numero: "))
            r = resta(a, b)
            print("El resultado es: ", r)

        if opcion == 3:
            a = int(input("Ingresa un numero: "))
            b = int(input("Ingresa otro numero: "))
            m = multiplicacion(a, b)
            print("El resultado es: ", m)

        if opcion == 4:
            a = int(input("Ingresa un numero: "))
            b = int(input("Ingresa otro numero: "))
            d = division(a, b)
            print("El resultado es: ", d)   


