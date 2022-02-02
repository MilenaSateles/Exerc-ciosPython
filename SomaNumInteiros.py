#Soma dos números de uma sequência númerica digitada pelo usuário

seq = int (input ("Digite um número inteiro: "))
soma = 0

while seq != 0:
    numero = seq % 10
    soma = soma + numero
    seq = seq // 10

print (soma)
