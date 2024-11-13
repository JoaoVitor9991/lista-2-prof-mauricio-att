import math 
def desvio_padrao(lista):
    media = sum(lista) / len(lista)
    soma_quadrado = 0
    for elementos in lista:
        soma_quadrado += (elementos - media) **2

    variante = soma_quadrado / len(lista)
    desvio_padrao = math.sqrt(variante)
    return desvio_padrao
