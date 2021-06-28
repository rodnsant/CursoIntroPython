largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

l = 1
h = 1

while altura >= h:
    while largura >= l:
        print("#",end="")
        l += 1
    else:
        print()
    h += 1
    l = 1