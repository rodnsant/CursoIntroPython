import math
def é_hipotenusa(n):
    a = 1
    b = 1

    while math.sqrt((a**2)+(b**2)) <= n:

        while math.sqrt((a**2)+(b**2)) <= n:
            if n**2 == ((a**2)+(b**2)):
                return True
            else:
                a += 1
        else:
            b += 1
            a = b
    
    return False


def soma_hipotenusas(n):

    soma = 0

    while n > 1:
        if é_hipotenusa(n) == True:
            soma += n
        n -= 1

    return soma