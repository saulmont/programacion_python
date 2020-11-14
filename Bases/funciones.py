# FUNCIONES

"""
Las funciones contienen lineas de codigo para ejecutar una tarea especifica.

Las funciones permiten reutilizar el codigo.

Para crear una funcion en python se utiliza la palabra reservada def.

Las funciones pueden recibir argumentos(parametros) y retornar valores si el programa asi lo requiere.

Ejemplo:
    def funcion_sumar(a, b):
        return a + b
"""

def saludar():
    """
        Esta funcion imprime un mensaje en pantalla.
        No recibe argumentos ni retorna nada.
    """
    print("Hola Mundo!")
    
def saludar_usuario(nombre):
    """
       Esta funcion imprime un saludo al usuario.
       Recibe el nombre del usuario como argumento; no retorna ningun valor.
    """
    print("Hola {}".format(nombre))

def sumar_numeros(numero_uno, numero_dos):
    """
      Esta funcion retorna el resultado de la suma de dos numeros que recibe como argumentos.
    """
    return numero_uno + numero_dos


if __name__ == "__main__": # Condicion que indica donde inicia la ejecucion del programa.
    saludar() # Llama a la funcion para ejecutarla.
    
    nombre = "Saúl"
    saludar_usuario(nombre)

    saludar_usuario("Lucas")

    a = 7
    b = 21
    resultado = sumar_numeros(a, b)
    print("{} + {} = {}".format(a, b, resultado))
