# Calcula raízes de equação de segundo grau a partir da definição de três funções.

import math

def delta(a, b, c):
    return (b ** 2) - 4 * a * c


def main():
    a = float (input ("Digite o valor de a: "))
    b = float (input ("Digite o valor de b: "))
    c = float (input ("Digite o valor de c: "))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if delta(a , b, c) < 0:
            print ("esta equação não possui raízes reais.")

    else:
            if d == 0:
                    X = (-b + math.sqrt(d))/(2*a)
                    print ("a raiz desta equação é",X)

            else:
                    X = (-b + math.sqrt(d))/(2*a)
                    Y = (-b - math.sqrt(d))/(2*a)
		
                    if X < Y:
                            print ("as raízes da equação são",X,"e",Y)
                    else:
                            print ("as raízes da equação são",Y,"e",X)

