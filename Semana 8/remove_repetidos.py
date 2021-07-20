def remove_repetidos(lista):
    listanorep = []
    lista.sort()
    for n in range(len(lista)):
        if lista[n] not in listanorep:
            listanorep.append(lista[n])
    
    return listanorep
