def sort(lista):
    for x in range(1, len(lista)):
        if x==1 and lista[x]<lista[x-1]: 
            lista[x-1], lista[x] = lista[x], lista[x-1]
            continue
        for y in range(x):
            if lista[x]<lista[y]:
                lista[x], lista[y] = lista[y], lista[x]
    return lista