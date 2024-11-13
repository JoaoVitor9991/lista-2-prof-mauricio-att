def conta_intervalo(lista, inicio, fim):
    contador =0

    for x in lista:
        if inicio <= x <= fim:
            contador +=1
    return contador