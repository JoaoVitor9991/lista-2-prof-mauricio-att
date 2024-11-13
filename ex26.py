def merge_sort(lista):
    
    if len(lista) <= 1:
        return lista

  
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

   
    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):
    
    resultado = []
    i, j = 0, 0



    return merge_sort 