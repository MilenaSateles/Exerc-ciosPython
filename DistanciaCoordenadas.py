#Calcula a distância entre dois pontos de um plano cartesiano
#Indica se a distância é curta ou longa

import math

x1 = int (input ("Digite a coordenada x1 de um ponto: "))
y1 = int ( input ("Digite a coordenada y1 de um ponto: "))
x2 = int ( input ("Digite a coordenada x2 de um ponto: "))
y2 = int ( input ("Digite a coordenada y2 de um ponto: "))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distancia >= 10:
	print ("longe")
else:
	print ("perto")
