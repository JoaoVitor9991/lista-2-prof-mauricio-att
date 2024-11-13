def diagonais_matriz(matriz):
    diagonal_principal = []
    diagonal_secundaria =[]

    n = len(matriz)

    for i in range(n):
        diagonal_principal.append(matriz[i][i])
        diagonal_secundaria.append(matriz[i][n  -1 -i])

    return diagonal_principal + diagonal_secundaria
