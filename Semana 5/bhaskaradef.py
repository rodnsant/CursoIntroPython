import math 

def raizdelta (): 
    return math.sqrt(delta)

def x1():
    return (-b + raizdelta())/(2*a)

def x2():
    return (-b - raizdelta())/(2*a)

a = float(input("Digite o valor de a: " ))

b = float(input("Digite o valor de b: " ))

c = float(input("Digite o valor de c: " ))

delta = (b**2) - (4*a*c)

if delta == 0:
    print("a raiz desta equação é",x1())
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        if x1() < x2():
            print("as raízes da equação são",x1(),"e",x2())
        else:
            print("as raízes da equação são",x2(),"e",x1())
