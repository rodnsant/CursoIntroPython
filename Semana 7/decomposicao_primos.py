n = int(input("Digite um número inteiro: "))

fator = 2

multiplicidade = 0

while n > 1:
    while n % fator == 0:
        n /= fator
        multiplicidade += 1
    else:
        if multiplicidade > 0:
            print (fator,"^",multiplicidade)
            fator +=1
            multiplicidade = 0
        else:
            fator +=1
