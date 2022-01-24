print("Cálculo de raiz quadrada")

import math

a = int(input("Digite o valor do coeficiente 'a' da equação:"))
b = int(input("Digite o valor do coeficiente 'b' da equação:"))
c = int(input("Digite o valor do coeficiente 'c' da equação:"))

delta = (b ** 2) - (4 * a * c)


if delta == 0:
	x1 = -b / (2 *a)
	print ("a raíz dupla desta equação é", x1)
else:
	if delta < 0:
		print("esta equação não possui raízes reais.")
	else:
		x1 = (-b + math.sqrt(delta))/ (2 *a)
		x2 = (-b - math.sqrt(delta))/ (2 *a)
		if x1 < x2 :
			print ("as raízes da equação são", x1, "e", x2)
		else:
			print ("as raízes da equação são", x2, "e", x1)