def fatorial(x):
    nfatorial = x

        if x == 0 or x == 1:
            nfatorial = 1
        else:
            while x != 1:
                nfatorial = nfatorial * (x - 1)
                x -= 1

def coeficiente_binomial(n,k):
    z = fatorial(n)/(fatorial(k)*fatorial(n-k))

n = int(input("Defina o número n: ")
k = int(input("Defina o número k: ")

print ("O coeficiente binomial de",n,"na classe",k,"é:",coeficiente_binomial(n,k))
