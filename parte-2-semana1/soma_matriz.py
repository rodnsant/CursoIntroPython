def soma_matrizes(m1, m2):
    
    n_linhas = len(m1)

    n_linhas_m2 = len(m2)

    n_colunas = len(m1[0])

    n_colunas_m2 = len(m2[0])

    m_soma = []

    if n_linhas == n_linhas_m2 and n_colunas == n_colunas_m2:
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                linha.append(m1[i][j]+m2[i][j])
            m_soma.append(linha)
        return m_soma
    else:
        return False