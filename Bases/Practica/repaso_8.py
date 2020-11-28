def suma(abc, defg, hijk):
    return abc + defg + hijk

def resta(abc, defg, hijk):
    return abc - defg - hijk

def multiplicacion(abc, defg, hijk):
    return abc * defg * hijk

def division(abc, defg):
    return abc / defg
    
for i in range(0, 101, 2):
    print("Cargando", i , "%  completo")

resultado = resta(4568, 98489, 152)
print("El resultado de la resta es: ", resultado)

resultado = suma(6489, 25654, 9845)
print("El resultado de la suma es: ", resultado)

resultado = multiplicacion(256, 159, 68)
print("El resultado de la Multiplicacion es: ", resultado)

resultado = division(4568, 48)
print("El resultado de la division es: ", resultado)