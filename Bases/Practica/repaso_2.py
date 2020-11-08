lucas = "luquitas"
comida = "croquetas"
gato_tusa = "Hoy me levante y el {0}, queria {1}, y awita.".format(lucas, comida)

gato_tus = "HOY ME LEVANTE Y EL {0}, QUERIA {1}, Y AWITA.".format(lucas, comida)

print(gato_tusa)

cat = gato_tusa.upper()

print(cat)

uvita = gato_tus.lower()

print(uvita)


titulo = "the poop that flows volume 1"

subtitulo = titulo.title()

print(subtitulo)

text = "Aquellos casos que hacen tus biñetas divertidas basado en la simple palabra de la comedia -El mañana se aproxima y caera sobre todos vosotros habeis escuchado pueblerinos, no obstante te terminan restringiendo del derecho de poder participar entre las personas presentes, porende terminas siendo desterrado -. mi lentilla jo jo jo"
reemplazo = "caspita"

texto = text.replace(".", reemplazo)
print(texto)

#Modo serio activado.png

lista = [1, 2, 3.6, 4, 3, 7.9]

lista2 = ["c", "d", "a", "b"]

lista3 = ["g","p","k","o","9","10","5.6","1","0","7.9"]

lista4 = ["864","b","ñ"]

lista.sort(reverse=True)
print(lista)

lista2.sort()
print(lista2)

lista3.extend(lista4)
print(lista3)