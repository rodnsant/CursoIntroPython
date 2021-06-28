def n_primos(n):

    k = 0

    divisor = 2

    primo = True
    
    while n >= 2:

        while divisor <= (n / 2) and primo:

            if (n % 2) == 0 or n % divisor == 0:
                primo = False
            else:
                divisor += +1
        else:
            if primo == False or n == 1:
                k += 0
                primo = True
                divisor = 2 
            else:
                k += 1
                primo = True
                divisor = 2
        n -= 1
    

    return k
