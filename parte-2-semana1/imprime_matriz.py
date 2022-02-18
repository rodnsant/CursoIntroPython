def imprime_matriz(matriz):

    n_linhas = len(matriz)

    n_colunas = len(matriz[0])

    for i in range(n_linhas):
        for j in range(n_colunas):
            if j == n_colunas - 1:
                print(matriz[i][j],end="")
            else:
                print(matriz[i][j],end=" ")
        print("")
