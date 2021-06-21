from OneDrive.Codes.testes import fatorial
n = int(input("Digite o valor de n: "))

nfatorial = n

if n == 0 or n == 1:
    nfatorial = 1
else:
    while n != 1:
        nfatorial = nfatorial * (n - 1)
        n -= 1

print (nfatorial)