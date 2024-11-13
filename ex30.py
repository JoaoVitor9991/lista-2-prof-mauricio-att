def histograma(lista):
    ocorre = {}
    for x in lista:
        if x in ocorre:
            ocorre[x] += 1
        else:
            ocorre[x] =1
    return ocorre 