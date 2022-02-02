#Indica se números digitados estão em ordem crescente ou não

num1 = int ( input ("Digite o primeiro número inteiro: "))
num2 = int ( input ("Digite o segundo número inteiro: "))
num3 = int ( input ("Digite o terceiro número inteiro: "))

if (num1 < num2) and (num2 < num3):
	print ("Boa! Está em ordem crescente!")
else:
	print ("Af! Não está em ordem crescente!")

