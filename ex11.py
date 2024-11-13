def produto_esccalar(v1, v2):
    soma = 0
    for i in range(len(v1)):
        soma += v1[i] * v2[i]
    return soma 