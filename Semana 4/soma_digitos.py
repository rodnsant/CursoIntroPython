numero = int(input("Digite um número inteiro: "))

soma = numero % 10

while numero != 0:
    numero //= 10
    soma += (numero % 10)

print (soma)