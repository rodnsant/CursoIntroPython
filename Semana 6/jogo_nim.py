def computador_escolhe_jogada(n,m):
    if n <= m:
        if n == 1:
            print("O computador tirou uma peça.")
            return n
        else:
            print("O computador tirou",n,"peças.")
            return n
    else:
        k = m
        while (n - k) % (m + 1) != 0:
            k -= 1
        else:
            if k == 0:
                print("O computador tirou",m,"peças.")
                return m
            else:
                print("O computador tirou",k,"peças.")
                return k

def usuario_escolhe_jogada(n,m):
    k = int(input("Quantas peças você vai tirar? "))
    while k > m or k <= 0 or k > n:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        k = int(input("Quantas peças você vai tirar? "))
    else:
        if k == 1:
            print("Você tirou uma peça.")
            return k
        else:
            print("Você tirou",k,"peças.")
            return k

def pecas_restantes(n,k):
    n -= k
    if n == 0:
        return n
    else:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
            return n
        else:
            print("Agora resta apenas",n,"peças no tabuleiro.\n")
            return n

def usuario_joga (n,m):
    k = usuario_escolhe_jogada(n,m)
    n = pecas_restantes(n,k)
    if n == 0:
        print("Fim do jogo! Você ganhou!\n")
        return n
    else:
        return n

def computador_joga(n,m):
    k = computador_escolhe_jogada(n,m)
    n = pecas_restantes(n,k)
    if n == 0:
        print("Fim do jogo! O computador ganhou!\n")
        return n
    else: 
        return n

def partida ():

    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while n < m:
        print("O número de peças deve ser maior que o limite de peças por jogada!")
        m = int(input("Limite de peças por jogada? "))
    else:
        if n%(m+1) == 0:
            print("\nVocê começa!\n")
            while n > 0:
                n = usuario_joga(n,m)
                if n == 0:
                    return False
                else:
                    n = computador_joga(n,m)
                    if n == 0:
                        return True

        else:
            print("\nComputador começa!\n")
            while n > 0:
                n = computador_joga(n,m)
                if n == 0:
                    return True
                else:
                    n = usuario_joga(n,m)
                    if n == 0:
                        return False

def campeonato():

    placarhumano = 0
    placarcomputador = 0
    rodada = 0

    print("\nVocê escolheu um campeonato!\n")

    while rodada < 3:
        rodada += 1
        print("**** Rodada",(rodada),"****")
        computadorganhou = partida()
        if computadorganhou == True:
            placarcomputador += 1
        else:
            placarhumano += 1
    else:
        print("**** Final do campeonato! ****\n")
        print("Placar: Você",placarhumano,"X",placarcomputador,"Computador\n")
    

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    sel = 3

    while sel > 2:
        print("1 - para jogar uma partida isolada")
        sel = int(input("2 - para jogar um campeonato "))
        if sel == 1:
            partida()
        else:
            if sel == 2:
                campeonato()
            else:
                print("\nOpção incorreta.\n")
                print("Escolha novamente:\n")
        
main()