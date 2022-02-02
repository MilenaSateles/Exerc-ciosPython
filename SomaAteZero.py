#Soma números digitados pelo usuário, até que ele digite o número zero.

print ("Digite uma sequência de números terminada por zero.")

soma = 0
valor = 1
while valor != 0:
    valor = int (input ("Valor a ser somado: "))
    soma = soma + valor

print ("A soma dos valores digitados é",soma)
