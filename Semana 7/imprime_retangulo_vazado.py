largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

l = 1
h = 1

while altura >= h:
    while h == 1 or h == altura:
        while largura >= l:
            print("#",end="")
            l += 1
        else:
            print()
        h += 1
        l = 1
    else:
        if h <= altura:
            while largura >= l:
                while l == 1 or l == largura:
                    print("#",end="")
                    l += 1
                while largura > 1 and largura > l:
                    print(" ",end="")
                    l += 1
            else:
                print()
        h += 1
        l = 1

