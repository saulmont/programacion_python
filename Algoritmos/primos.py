def es_primo(n):
    c = 0
    i = 1

    while i <= n:
        if n % i == 0:
            c = c + 1
        i = i + 1

    if c > 2:
        return False
    else:
        return True
    
if __name__ == '__main__':
    n = int(input("Ingresa un numero: "))
 
    if es_primo(n):
        print('Es primo')
    else:
        print('No es primo')