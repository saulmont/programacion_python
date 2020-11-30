var_numeral = 12 # esta variable es global y puede ser accedida desde cualquier lugar del codigo.

def crear_variable():
    var_numeral = 98 # esta variable es local y solo puede ser accedida desde esta funcion.
    print(var_numeral)

def modificar_variable():
    global var_numeral # esta accediendo a la variable global. 
    var_numeral = 1569 # esta modificando el valor de la variable global.

print(var_numeral) # imprime la variable global antes de que se modifique.

modificar_variable() # esta llamando a  funcion.

print(var_numeral) # esta imprimiendo la variable global despues de su modificacion.

