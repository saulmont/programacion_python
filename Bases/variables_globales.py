# VARIABLES GLOBALES

variable = "Saúl" # Esta variable existe fuera de la funcion y es una VARIABLE GLOBAL.

def cambiar_variable():
    print("Llamando funcion")
    variable = "Lucas" # Esta variable existe SOLO dentro de la funcion y es una VARIABLE LOCAL.

def otra_funcion():
    global variable # Accede a la variable global que se le indique.
    variable = "Lucas"

print(variable)
otra_funcion()
print(variable)
