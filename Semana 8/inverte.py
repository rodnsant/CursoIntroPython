lista = []

x = -1

while x != 0:
    x = int(input("Digite um número: "))
    if x != 0:
        lista.append(x)

lista.reverse()

for n in range(len(lista)):
    print(lista[n])
