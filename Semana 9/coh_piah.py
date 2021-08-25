import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    assinatura_comparada = []

    zip_obj = zip(as_a,as_b)

    for as_a_i, as_b_i in zip_obj:
        assinatura_comparada.append(abs(as_a_i - as_b_i))

    return sum(assinatura_comparada) / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    lista_sentencas = separa_sentencas(texto)

    lista_frases = []

    lista_n_caracteres_sentenca = []

    for sentenca in lista_sentencas:
        lista_frases.extend(separa_frases(sentenca))
        lista_n_caracteres_sentenca.append(len(sentenca))

    lista_palavras = []

    lista_n_caracteres_frase = []

    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
        lista_n_caracteres_frase.append(len(frase))

    lista_n_palavras_texto = []

    for palavra in lista_palavras:
        lista_n_palavras_texto.append(len(palavra))
 
    wal_texto = sum(lista_n_palavras_texto) / len(lista_n_palavras_texto)

    ttr_texto = n_palavras_diferentes(lista_palavras) / len(lista_palavras)

    hlr_texto = n_palavras_unicas(lista_palavras) / len(lista_palavras)

    sal_texto = sum(lista_n_caracteres_sentenca) / len(lista_sentencas)

    sac_texto = len(lista_frases) / len(lista_sentencas)
    
    pal_texto = sum(lista_n_caracteres_frase) / len(lista_frases)

    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass
