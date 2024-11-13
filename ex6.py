def diferenca_conjuntos(l1, l2):
    x = []
    for i in l1:
        if i not in l2:
            x.append(i)
    return x
