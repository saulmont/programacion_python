# FORMATO DE CADENAS DE TEXTO

# Formateando cadenas de texto.
nombre_uno = "Saúl"
nombre_dos = "Lucas"

mensaje = "Hola {0}, yo me llamo {1}.".format(nombre_uno, nombre_dos)

mensaje = "Hola {nombre_uno}, yo me llamo {nombre_dos}.".format(nombre_dos=nombre_uno, nombre_uno=nombre_dos)

print(mensaje)

# Mayusculas y minusculas

nombre_mayusculas = nombre_uno.upper()

# Imprime el nombre con mayusculas. 
print(nombre_mayusculas)

nombre_minusculas = nombre_dos.lower()

# Imprime el nombre con minusculas.

print(nombre_minusculas)

titulo = "hola mundo!!!"

titulo = titulo.title()

# Imprime el texto como titulo.
print(titulo)

# BUSQUEDA DENTRO DE CADENAS DE TEXTO

texto = "El Saúl se levanto en la mañana, hizo arroz con huevo para su desayuno; luego alimento al gato."

# Buscar palabras y caracteres.
busqueda = texto.find("gato")
print(texto[busqueda:-1])

# Contar palabras y caracteres.
contador = texto.count("gato")
print(contador)

# MANIPULAR CADENAS DE TEXTO

texto = "El Saúl se levanto en la mañana, hizo arroz con huevo para su desayuno; luego alimento al gato."

# Reemplazar palabras o caracteres.
texto = texto.replace("gato", nombre_dos)
print(texto)

# Cortar cadenas de texto
dividido = texto.split(" ")
print(dividido)
print(dividido[8])
