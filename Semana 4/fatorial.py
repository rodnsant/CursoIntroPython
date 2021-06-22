n = int(input("Digite o valor de n: "))

nfat = 1

while n > 1:
    nfat = nfat * n
    n -= 1

print (nfat)