def media_ponderada(lista_valores, lista_pesos):
    soma_produtos = 0
    soma_pesos = 0

    for valor, peso in zip(lista_valores, lista_pesos):
        soma_produtos += valor * peso 
        soma_pesos += peso

    if soma_pesos == 0:
        raise ValueError("A soa dos pesos n pode ser zero")
    
    media = soma_produtos / soma_pesos

    return media 