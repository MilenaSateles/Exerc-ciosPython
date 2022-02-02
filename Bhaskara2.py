#Resolve uma equação de segundo grau aplicando a fórmula de Bhaskara
#Aponta se a equação não possui raízes reais, ou se possui uma ou duas raízes


import math

a = float (input ("Digite o valor de a: "))
b = float (input ("Digite o valor de b: "))
c = float (input ("Digite o valor de c: "))

delta = (b ** 2) - 4 * a * c

if delta < 0:
	print ("esta equação não possui raízes reais.")

else:
	if delta == 0:
		X = (-b + math.sqrt(delta))/(2*a)
		print ("a raiz desta equação é",X)

	else:
		X = (-b + math.sqrt(delta))/(2*a)
		Y = (-b - math.sqrt(delta))/(2*a)
		
		if X < Y:
			print ("as raízes da equação são",X,"e",Y)
		else:
			print ("as raízes da equação são",Y,"e",X)
