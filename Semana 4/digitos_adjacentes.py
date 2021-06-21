numero = int(input("Digite um número inteiro: "))

digitosiguais = False

while not digitosiguais and numero != 0:
    ultimodigito = numero % 10
    numero //= 10
    penultimodigito = numero % 10
    if ultimodigito == penultimodigito:
        digitosiguais = True
else:    
    if digitosiguais:
        print ("sim")
    else:
        print ("não")