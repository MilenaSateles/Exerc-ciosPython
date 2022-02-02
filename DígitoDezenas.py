#Indica o dígito das dezenas do número inteiro digitado

numero = int(input("Digite um número inteiro: "))
dezena = numero // 10
centena = dezena % 10
print ("O dígito das dezenas é",centena)
