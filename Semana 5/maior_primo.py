def éPrimo(k):

    divisor = 2

    primo = True

    while divisor < (k / 2) and primo:

        if (k % 2) == 0 or k % divisor == 0:
            return False
        else:
            divisor += +1
    else:
        if primo == False or k == 1:
            return False
        else:
            return True


def maior_primo(x):

    while éPrimo(x) == False:
        x -= 1
    else:
        return x
