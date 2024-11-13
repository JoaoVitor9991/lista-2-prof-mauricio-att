def multi_pares(lista):
    produto = 1
    tem_par = False

    for x in lista:
        if x % 2 == 0:
            produto *= x 
            tem_par = True
        
    
    return produto 