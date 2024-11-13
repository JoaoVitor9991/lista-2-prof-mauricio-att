def separa_pares_impares(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 ==0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares