def selection_sort(lista):
    for x in range (len(lista)-1):
        menor = x
        for j in range(x+1 , len(lista)):
            if lista[j] < lista[menor]:
                menor = j

        if menor != x:
            lista[x],lista[menor] = lista[menor], lista[x]

    return lista
