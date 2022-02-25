# Função recebe 3 valores inteiros e devolve o maior entre eles.

def maximo(x, y, z):
    if (x > y) and (x > z):
        return x
    if (y > x) and (y > z):
        return y
    if (z > x) and (z > y):
        return z
    
    if (x == z) and (x == y) and (y == z):
        return x
   
    
