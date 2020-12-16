# FUNCIONES CON ARGUMENTOS

def suma(*args):
    resultado = 0
    for i in args:
        resultado = resultado + i
    return resultado

def argumentos(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs['taita'])

if __name__ == '__main__':
    print(suma(7, 7))
    print(suma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

    argumentos(taita='Significa papá en el idioma kechwa', apellido='Montalvo', mascota='El gato Lucas')
