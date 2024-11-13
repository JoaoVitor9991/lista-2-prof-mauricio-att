def quick_sort(lista):
    pilha = [(0, len(lista)- 1) ]

    while pilha:
        inicio, fim = pilha.pop()

        if inicio < fim:
            pivo = particiona(lista, inicio, fim)

            pilha.append((inicio,pivo-1))
            pilha.append((pivo + 1, fim))

    return lista

def particiona(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio -1 
    for j in range(inicio, fim):
        if lista[j] < pivo:
            i += 1
            lista[i], lista[j] = lista[ j], lista[i +1]
    return i +1