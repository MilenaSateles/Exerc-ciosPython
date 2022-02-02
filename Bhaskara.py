#Resolve uma equação de segundo grau aplicando a fórmula de Bhaskara
#Aponta se a equação não possui raízes reais, ou se possui uma ou duas raízes

import math

a = float (input ("Digite o valor de a: "))
b = float (input ("Digite o valor de b: "))
c = float (input ("Digite o valor de c: "))

delta = (b ** 2) - 4 * a * c

if delta == 0:
   x = (-b + math.sqrt(delta))/(2*a)
   print ("A única raiz da equação é",x)

else:
   if delta < 0:
      print ("A equação não possui raízes reais.")

   else:
      x1 = (-b + math.sqrt(delta))/(2*a)
      x2 = (-b - math.sqrt(delta))/(2*a)
      print ("As raízes da equação são:",x1,"e",x2)
