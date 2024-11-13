def firenca_elementos_lista(lista):
    diferencas = []
    for i in range(len(lista)- 1):
        diferencas = abs(lista[i +1] - lista [i])
        diferencas.append(diferencas)
    return diferencas