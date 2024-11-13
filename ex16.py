def busca_binaria(lista, elemento):
    esquerda = 0
    direita= len(lista)-1

    while esquerda <= direita:
        meio= (esquerda + direita) // 2

        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            direita = meio -1
        else:
            esquerda = meio +1
    return -1