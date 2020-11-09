# DICCIONARIOS

"""
Igual que con las listas y tuplas los diccionarios pueden recibir cualquier tipo de variable.
Los diccionarios pueden ser facilmente modificados.
Para crear un diccionario se utilizan las llaves {}.
Los diccionarios manejan Clave y Valor.
"""

diccionario = {
            "nombre": "Lucas", 
            "juguetes": ["Cuerda", "Collar", "Pelota"], 
            "es_gato": True, 
            "comida": ("Croquetas", "Camarones")
        }

print(diccionario)

# Accede al valor del nombre en el diccionario.
print(diccionario["nombre"])

# Agregar un nuevo valor al diccionario.
diccionario["edad"] = 1
print(diccionario)

# Modificar un valor del diccionario.
diccionario["comida"] = ("Croquetas", "Camarones", "Carne en trozitos pequeños")
print(diccionario)

# Eliminar una clave y valor del diccionario.
del diccionario["edad"]
print(diccionario)

# Unir dos diccionarios.
diccionario_dos = {"padre": "Lucas primero"}
diccionario.update(diccionario_dos)
print(diccionario)

# Obtener las claves del diccionario.
claves = diccionario.keys()
print(claves)

# Obtener los valores del diccionario.
valores = diccionario.values()
print(valores)
