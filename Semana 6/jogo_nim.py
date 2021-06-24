def computador_escolhe_jogada(n,m):
    if n > 0 > m:
        True


def usuario_escolhe_jogada(n,m):
    p = int(input("Quantas peças você vai tirar? "))
    while p > (m+1) or p <= 0 or p > n:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        p = int(input("Quantas peças você vai tirar? "))
    else:
        n -= p
        if p == 1:
            print("Você tirou uma peça.")
            return n
        else:
            print("Você tirou",p,"peças.")
            return n
        


def partida ():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while n < m:
        print("O número de peças deve ser maior que o limite de peças por jogada!")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    else:
        if n%(m+1) == 0:
            print("\nVocê começa!\n")
            while n > 0:
                n = usuario_escolhe_jogada(n,m)
                if n == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    return False
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora resta apenas",n,"peças no tabuleiro.\n")
                n = computador_escolhe_jogada(n,m)
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
                n = computador_escolhe_jogada(n,m)
                if n == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    return True
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora resta apenas",n,"peças no tabuleiro.\n")
                n = usuario_escolhe_jogada(n,m)
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

    print("Você escolheu um campeonato!\n")

    while rodada < 3:
        print("**** Rodada,",(rodada+1),"****\n")
        computadorganhou = partida()
        if computadorganhou == True:
            placarcomputador += 1
        else:
            placarhumano += 1
    else:
        print("**** Final do campeonato! ****\n")
        print("Placar: Você",placarhumano,"X",placarcomputador,"Computador ****\n")
    

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    sel = int(input("2 - para jogar um campeonato "))
    if sel == 1:
        partida()
    else:
        campeonato()

main()