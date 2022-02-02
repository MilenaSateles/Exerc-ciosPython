#Recebe número inteiro positivo e verifica se é um número primo.

n = int (input("Digite um número inteiro: "))
i = 2

while n % i != 0:
    i = i + 1

if i == n:
     print ("primo")
else:
    print ("não primo")
