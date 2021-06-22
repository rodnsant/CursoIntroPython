def fatorial(n):
    nfat = 1
    while n > 1:
        nfat = nfat * n
        n -= 1
    return nfat

def coeficiente_binomial(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))


n = int(input("Defina o número n, positivo: "))
k = int(input("Defina o número k, positivo: "))

while n < k or n < 0 or k < 0:
    print ("Por favor, defina 'n' maior ou igual a 'k' e ambos positivos")
    n = int(input("Defina o número n: "))
    k = int(input("Defina o número k: "))
else:
    x = coeficiente_binomial(n,k)

print ("O coeficiente binomial de",n,"na classe",k,"é igual a",x)