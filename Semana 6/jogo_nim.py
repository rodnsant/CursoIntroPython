def computador_escolhe_jogada(n,m):
    if n <= m:
        return n
    else:
        p = m
        while (n - p) % (m + 1) != 0:
            p -= 1
        else:
            return p

def usuario_escolhe_jogada(n,m):
    p = int(input("Quantas peças você vai tirar? "))
    while p > m or p <= 0 or p > n:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        p = int(input("Quantas peças você vai tirar? "))
    else:
        return p

def partida ():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while n < m:
        print("O número de peças deve ser maior que o limite de peças por jogada!")
        m = int(input("Limite de peças por jogada? "))
    else:
        if n%(m+1) == 0:
            print("\nVocê começa!\n")
            while n > 0:
                p = usuario_escolhe_jogada(n,m)
                if p == 1:
                    print("Você tirou uma peça.")
                else:
                    print("Você tirou",p,"peças.")
                n -= p
                if n == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    return False
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora resta apenas",n,"peças no tabuleiro.\n")
                p = computador_escolhe_jogada(n,m)
                if p == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou",p,"peças.")
                n -= p
                if n == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    return True
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora resta apenas",n,"peças no tabuleiro.\n")
        else:
            print("\nComputador começa!\n")
            while n > 0:
                p = computador_escolhe_jogada(n,m)
                if p == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou",p,"peças.")
                n -= p
                if n == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    return True
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora resta apenas",n,"peças no tabuleiro.\n")
                p = usuario_escolhe_jogada(n,m)
                if p == 1:
                    print("Você tirou uma peça.")
                else:
                    print("Você tirou",p,"peças.")
                n -= p
                if n == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    return False
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora resta apenas",n,"peças no tabuleiro.\n")


def campeonato():

    placarhumano = 0
    placarcomputador = 0
    rodada = 0

    print("\nVocê escolheu um campeonato!\n")

    while rodada < 3:
        rodada += 1
        print("**** Rodada",(rodada),"****\n")
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
                print("Escolha novamente\n")
        
main()