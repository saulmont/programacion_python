# CONDICIONALES

"""
Sirven para realizar comparaciones entre variables, y comprobar que una condiciones se cumpla, 
es decir, si esta es verdadera o falsa.

Existen tres sentencias para realizar una comparacion:

1. IF(si).

2. ELIF(si no).

3. ELSE(caso contrario).

Para realizar comparaciones se utilizan las siguientes expresiones:

1. Mayor que(>).
2. Menor que(<).
3. Igual(==).
4. Mayor o igual(>=).
5. Menor o igual(<=).
6. Diferente de(!=).

Ejemplo de uso:

    if condicion:
        ################
        ################
        #####BLOQUE#####
        ################
        ################

"""

VERDADERO = True
FALSO = False

if VERDADERO:
    print("La condicion se cumple por que es VERDADERA.")
else:
    print("La condicion no se cumple por que es FALSA.")
    
a = 5
b = 4
c = 7

if a == b:
    print("{} y {} son iguales".format(a, b))
else:
    print("{} y {} no son iguales".format(a, b))

if a > b:
    print("{} es mayor a {}".format(a, b))

if b < a:
    print("{} es menor {}".format(b, a))

if a >= b:
    print("{} es mayor o igual a {}".format(a, b))

if b <= a:
    print("{} es menor o igual a {}".format(b, a))

if a != b:
    print("{} es diferente de {}".format(a, b))

if 1 == '1':
    print("INICIO BLOQUE #1")
    print("Son iguales")
    print("FIN BLOQUE #1")
else:
    print("INICIO BLOQUE #2")
    print("No son iguales")
    print("FIN BLOQUE #2")

print("FUERA DEL BLOQUE")

#  5   4
if a < b:
    print("{} es menor {}".format(a, b))
#    5   7
elif a < c:
    print("{} es menor {}".format(a, c))
else:
    print("{} no es el menor".format(a))
