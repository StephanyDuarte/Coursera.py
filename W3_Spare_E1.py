import math

x1 = float(input("Ponto 1: Digite a coordenada x: "))
y1 = float(input("Ponto 1: Digite a coordenada y: "))
x2 = float(input("Ponto 2: Digite a coordenada x: "))
y2 = float(input("Ponto 2: Digite a coordenada y: "))

d = ( x1 - x2) ** 2 + (y1 - y2) ** 2
D = math.sqrt(d)

if D >= 10:
	print("longe")
else:
	print("perto")