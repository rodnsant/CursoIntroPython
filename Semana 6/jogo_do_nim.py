def computador_escolhe_jogada(n,m):
    if n > 0:
        True


def usuario_escolhe_jogada(n,m):
    p = int(input("\nQuantas peças você vai tirar? "))
    while p > (m+1) or p <= 0:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        p = int(input("Quantas peças você vai tirar? "))
    else:
        n -= p
        if p == 1:
            print("Você tirou uma peça")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
                return n
            else:
                print("Agora resta apenas",n,"peças no tabuleiro.\n")
                return n
        else:
            print("\nVocê tirou",p,"peças do tabuleiro")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
                return n
            else:
                print("Agora resta apenas",n,"peças no tabuleiro.\n")
                return n
        


def partida ():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n < m:
        print("O número de peças deve ser maior que o limite de peças por jogada!")
    else:
        if n%(m+1) == 0:
            print("\nVocê começa!")
            while n > 0:
                n = usuario_escolhe_jogada(n,m)
                if n == 0:
                    print("\nFim do jogo! Você ganhou!\n")
                    return False
                else:
                    n = computador_escolhe_jogada(n,m)
                    if n == 0:
                        print("\nFim do jogo! O computador ganhou!\n")
                        return True


        else:
            print("\nComputador começa!")
            while n>0:
                computador_escolhe_jogada(n,m)



            usuario_escolhe_jogada(n,m)

def campeonato():

    placarhumano = 0

    placarcomputador = 0

    print("Você escolheu um campeonato!\n")

    print("**** Rodada 1 ****\n")

    computadorganhou = partida()

    if computadorganhou == True:
        placarcomputador += 1
    else:
        placarhumano += 1
    
    print("**** Rodada 2 ****\n")

    computadorganhou = partida()

    if computadorganhou == True:
        placarcomputador += 1
    else:
        placarhumano += 1

    print("**** Rodada 3 ****\n")

    computadorganhou = partida()

    if computadorganhou == True:
        placarcomputador += 1
    else:
        placarhumano += 1

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