diccionario = {
        "Nombre": "Uvita",
        "jugetes": ["cualquier cosa", "Pelota"],
        "es_perrita": True,    
        "meses": 2,
        "iniciales": "uma",
        "primera_inicial": ("U", "M")
    } 

print(diccionario)
print(diccionario["Nombre"])

diccionario1 = {"Padre": "desconocido"}
diccionario.update(diccionario1)
print(diccionario)

claves = diccionario.keys()
print(claves)

valores = diccionario.values()
print(valores)

del diccionario1["Padre"]
print(diccionario1)