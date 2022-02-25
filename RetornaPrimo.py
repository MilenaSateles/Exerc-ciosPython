#função recebe número inteiro maior ou igual a 2 e devolve o maior número primo
#menor ou igual ao número passado à função

def ePrimo(k):
    
    i = 2
    while k % i != 0:
        i = i + 1

    if i == k:
        return True
    else:
        return False

def maior_primo(k):
    while ePrimo(k) != True:
        k = k - 1
    return k



        




    
