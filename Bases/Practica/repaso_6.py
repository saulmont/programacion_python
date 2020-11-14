# resultado = 1
# contador = 1
# limite = 5

# while contador <= limite:
#     # print(contador)
#     resultado = contador * resultado
#     contador = contador + 1
# print(resultado)

def factorial(numero):
    resultado = 1
    contador = 1
    
    while contador <= numero:
        resultado = contador * resultado
        contador = contador + 1
    return resultado

if __name__ == "__main__":
    numero = int(input("ingresa un numero: "))
    fun = factorial(numero)
    print("El resultado es:", fun)
