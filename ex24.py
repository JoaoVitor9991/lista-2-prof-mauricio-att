import math
def numeros_primos(n):
    primos =[]
    for numero in range(2, n +1):
        eh_primo= True

        for i in range(2, int(math.sqrt(numero))+ 1):
            if numero % i == 0:
                eh_primo = False
                break

        if eh_primo:
            primos.append(numero)
    return primos