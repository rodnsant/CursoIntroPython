n = int(input("Digite um número inteiro: "))

divisor = 2

primo = True

while divisor < (n / 2) and primo:

    if n % divisor == 0:
        primo = False
    else:
        divisor += +1
else:
    if primo == False or n == 1:
        print ("não primo")
    else:
        print ("primo")
