def conta_consoante(texto):
    cont = 0
    texto_minusculo=texto.lower()
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for x in texto_minusculo:
        if x in consoantes:
            cont +=1

    return cont 