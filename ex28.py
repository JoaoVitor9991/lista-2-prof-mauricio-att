def remove_multiplos(lista, n):
    nova_lista = [elemento for elemento in lista if elemento % n !=0]
    return nova_lista